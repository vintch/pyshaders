from pyglet.gl import glUniform1iv, glActiveTexture, glEnable, glBindTexture, GLint, GL_TEXTURE_2D, GL_TEXTURE0
from pyglet.image import Texture


# Taken from
# https://github.com/google/swiftshader/blob/master/include/GL/glcorearb.h
GL_SAMPLER_2D      = 0x8B5E
GL_SAMPLER_2D_RECT = 0x8B63


def uniform_sampler2D_setter_impl(loc, count, get_data_ptr_func, value, accessor, rectangle):
    if "texture_unit_bindings" not in accessor.__extensions_storage__:
        accessor.__extensions_storage__["texture_unit_bindings"] = dict([(-1, -1)])  # max + 1 == 0
    bindings = accessor.__extensions_storage__["texture_unit_bindings"]
    loc_str = str(loc)
    if type(value) is int:
        texture_unit = value
    elif isinstance(value, Texture):
        if (value.target != GL_TEXTURE_2D) ^ rectangle:
            raise ValueError("Texture expected to be {} rectangle".format("a" if rectangle else "not a"))
        if loc_str not in bindings:
            texture_unit = max(bindings.values()) + 1
            bindings[loc_str] = texture_unit
        else:
            texture_unit = bindings[loc_str]
        glActiveTexture(GL_TEXTURE0 + texture_unit)
        glEnable(value.target)
        glBindTexture(value.target, value.id)
    else:
        raise TypeError("Sampler2D uniform got value of unsupported type")
    glUniform1iv(loc, count, get_data_ptr_func(texture_unit))


def uniform_sampler2D_setter(loc, count, get_data_ptr_func, value, accessor):
    uniform_sampler2D_setter_impl(loc, count, get_data_ptr_func, value, accessor, False)


def uniform_sampler2DRect_setter(loc, count, get_data_ptr_func, value, accessor):
    uniform_sampler2D_setter_impl(loc, count, get_data_ptr_func, value, accessor, True)


def supported():
    return True


def load(mod):
    # Add uniform data
    uniform_data = {
        GL_SAMPLER_2D:      (GLint, 1, uniform_sampler2D_setter),
        GL_SAMPLER_2D_RECT: (GLint, 1, uniform_sampler2DRect_setter)
    }
    mod.UNIFORMS_DATA.update(uniform_data)
