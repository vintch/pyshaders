from rpi_gles2_native import glUniform1iv, glActiveTexture, GLint, glBindTexture, \
    GL_TEXTURE0, GL_SAMPLER_2D


def uniform_sampler2D_setter(loc, count, get_data_ptr_func, value, accessor):
    if "texture_unit_bindings" not in accessor.__extensions_storage__:
        accessor.__extensions_storage__["texture_unit_bindings"] = dict([(-1, -1)])  # max + 1 == 0
    bindings = accessor.__extensions_storage__["texture_unit_bindings"]
    loc_str = str(loc)
    if type(value) is int:
        texture_unit = value
    elif hasattr(value, "target") and hasattr(value, "id"):
        if loc_str not in bindings:
            texture_unit = max(bindings.values()) + 1
            bindings[loc_str] = texture_unit
        else:
            texture_unit = bindings[loc_str]
    else:
        raise TypeError("Sampler2D uniform got value of unsupported type")
    glActiveTexture(GL_TEXTURE0 + texture_unit)
    if type(value) is not int:
        glBindTexture(value.target, value.id)
    glUniform1iv(loc, count, get_data_ptr_func(texture_unit))


def supported():
    return True


def load(mod):
    # Add uniform data
    uniform_data = {
        GL_SAMPLER_2D:      (GLint, 1, uniform_sampler2D_setter)
    }
    mod.UNIFORMS_DATA.update(uniform_data)
