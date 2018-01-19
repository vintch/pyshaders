# Minimal partial GLESv2 python wrapper

GLES2_LIB = "libbrcmGLESv2.so"

#####################################################################

GL_ARRAY_BUFFER = 0x8892
GL_ELEMENT_ARRAY_BUFFER = 0x8893
GL_STATIC_DRAW = 0x88E4
GL_DYNAMIC_DRAW = 0x88E8
GL_BUFFER_SIZE = 0x8764
GL_BUFFER_USAGE = 0x8765
GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31
GL_SHADER_TYPE = 0x8B4F
GL_DELETE_STATUS = 0x8B80
GL_LINK_STATUS = 0x8B82
GL_VALIDATE_STATUS = 0x8B83
GL_ATTACHED_SHADERS = 0x8B85
GL_ACTIVE_UNIFORMS = 0x8B86
GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
GL_ACTIVE_ATTRIBUTES = 0x8B89
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
GL_CURRENT_PROGRAM = 0x8B8D
GL_FLOAT_VEC2 = 0x8B50
GL_FLOAT_VEC3 = 0x8B51
GL_FLOAT_VEC4 = 0x8B52
GL_INT_VEC2 = 0x8B53
GL_INT_VEC3 = 0x8B54
GL_INT_VEC4 = 0x8B55
GL_FLOAT_MAT2 = 0x8B5A
GL_FLOAT_MAT3 = 0x8B5B
GL_FLOAT_MAT4 = 0x8B5C
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
GL_FALSE = 0
GL_TRUE = 1
GL_COMPILE_STATUS = 0x8B81
GL_INFO_LOG_LENGTH = 0x8B84
GL_SHADER_SOURCE_LENGTH = 0x8B88
GL_TEXTURE_2D = 0x0DE1
GL_TEXTURE0 = 0x84C0

#####################################################################

from ctypes import *

GLvoid_p = c_void_p
GLenum = c_uint
GLenum_p = POINTER(GLenum)
GLboolean = c_ubyte
GLboolean_p = POINTER(GLboolean)
GLbyte = c_byte
GLbyte_p = POINTER(GLbyte)
GLchar_p = c_char_p
GLshort = c_short
GLshort_p = POINTER(GLshort)
GLint = c_int
GLint_p = POINTER(GLint)
GLubyte = c_ubyte
GLubyte_p = POINTER(GLubyte)
GLushort = c_short
GLushort_p = POINTER(GLushort)
GLuint = c_uint
GLuint_p = POINTER(GLuint)
GLfloat = c_float
GLfloat_p = POINTER(GLfloat)
GLintptr = c_long
GLintptr_p = POINTER(GLintptr)
GLsizeiptr = c_long
GLsizeiptr_p = POINTER(GLsizeiptr)
GLsizei = c_int
GLsizei_p = POINTER(GLsizei)

gles2 = CDLL(GLES2_LIB)

#####################################################################

""" GL_APICALL void         GL_APIENTRY glAttachShader (GLuint program, GLuint shader); """
gles2.glAttachShader.restype = None
gles2.glAttachShader.argtypes = (GLuint, GLuint)  # program, shader
glAttachShader = gles2.glAttachShader

""" GL_APICALL void         GL_APIENTRY glBindBuffer (GLenum target, GLuint buffer); """
gles2.glBindBuffer.restype = None
gles2.glBindBuffer.argtypes = (GLenum, GLuint)  # target, buffer
glBindBuffer = gles2.glBindBuffer

""" GL_APICALL void         GL_APIENTRY glBufferData (GLenum target, GLsizeiptr size, const GLvoid* data, GLenum usage); """
gles2.glBufferData.restype = None
gles2.glBufferData.argtypes = (GLenum, GLsizeiptr, GLvoid_p, GLenum)  # target, size, data, usage
glBufferData = gles2.glBufferData

""" GL_APICALL void         GL_APIENTRY glBufferSubData (GLenum target, GLintptr offset, GLsizeiptr size, const GLvoid* data); """
gles2.glBufferSubData.restype = None
gles2.glBufferSubData.argtypes = (GLenum, GLintptr, GLsizeiptr, GLvoid_p)  # target, offset, size, data
glBufferSubData = gles2.glBufferSubData

""" GL_APICALL void         GL_APIENTRY glCompileShader (GLuint shader); """
gles2.glCompileShader.restype = None
gles2.glCompileShader.argtypes = (GLuint,)  # shader
glCompileShader = gles2.glCompileShader

""" GL_APICALL GLuint       GL_APIENTRY glCreateProgram (void); """
gles2.glCreateProgram.restype = GLuint
gles2.glCreateProgram.argtypes = ()  #
glCreateProgram = gles2.glCreateProgram

""" GL_APICALL GLuint       GL_APIENTRY glCreateShader (GLenum type); """
gles2.glCreateShader.restype = GLuint
gles2.glCreateShader.argtypes = (GLenum,)  # type
glCreateShader = gles2.glCreateShader

""" GL_APICALL void         GL_APIENTRY glDeleteBuffers (GLsizei n, const GLuint* buffers); """
gles2.glDeleteBuffers.restype = None
gles2.glDeleteBuffers.argtypes = (GLsizei, GLuint_p)  # n, buffers
glDeleteBuffers = gles2.glDeleteBuffers

""" GL_APICALL void         GL_APIENTRY glDeleteProgram (GLuint program); """
gles2.glDeleteProgram.restype = None
gles2.glDeleteProgram.argtypes = (GLuint,)  # program
glDeleteProgram = gles2.glDeleteProgram

""" GL_APICALL void         GL_APIENTRY glDeleteShader (GLuint shader); """
gles2.glDeleteShader.restype = None
gles2.glDeleteShader.argtypes = (GLuint,)  # shader
glDeleteShader = gles2.glDeleteShader

""" GL_APICALL void         GL_APIENTRY glDetachShader (GLuint program, GLuint shader); """
gles2.glDetachShader.restype = None
gles2.glDetachShader.argtypes = (GLuint, GLuint)  # program, shader
glDetachShader = gles2.glDetachShader

""" GL_APICALL void         GL_APIENTRY glDisableVertexAttribArray (GLuint index); """
gles2.glDisableVertexAttribArray.restype = None
gles2.glDisableVertexAttribArray.argtypes = (GLuint,)  # index
glDisableVertexAttribArray = gles2.glDisableVertexAttribArray

""" GL_APICALL void         GL_APIENTRY glEnableVertexAttribArray (GLuint index); """
gles2.glEnableVertexAttribArray.restype = None
gles2.glEnableVertexAttribArray.argtypes = (GLuint,)  # index
glEnableVertexAttribArray = gles2.glEnableVertexAttribArray

""" GL_APICALL void         GL_APIENTRY glGenBuffers (GLsizei n, GLuint* buffers); """
gles2.glGenBuffers.restype = None
gles2.glGenBuffers.argtypes = (GLsizei, GLuint_p)  # n, buffers
glGenBuffers = gles2.glGenBuffers

""" GL_APICALL void         GL_APIENTRY glGetActiveAttrib (GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name); """
gles2.glGetActiveAttrib.restype = None
gles2.glGetActiveAttrib.argtypes = (GLuint, GLuint, GLsizei, GLsizei_p, GLint_p, GLenum_p, GLchar_p)  # program, index, bufsize, length, size, type, name
glGetActiveAttrib = gles2.glGetActiveAttrib

""" GL_APICALL void         GL_APIENTRY glGetActiveUniform (GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name); """
gles2.glGetActiveUniform.restype = None
gles2.glGetActiveUniform.argtypes = (GLuint, GLuint, GLsizei, GLsizei_p, GLint_p, GLenum_p, GLchar_p)  # program, index, bufsize, length, size, type, name
glGetActiveUniform = gles2.glGetActiveUniform

""" GL_APICALL void         GL_APIENTRY glGetAttachedShaders (GLuint program, GLsizei maxcount, GLsizei* count, GLuint* shaders); """
gles2.glGetAttachedShaders.restype = None
gles2.glGetAttachedShaders.argtypes = (GLuint, GLsizei, GLsizei_p, GLuint_p)  # program, maxcount, count, shaders
glGetAttachedShaders = gles2.glGetAttachedShaders

""" GL_APICALL int          GL_APIENTRY glGetAttribLocation (GLuint program, const GLchar* name); """
gles2.glGetAttribLocation.restype = int
gles2.glGetAttribLocation.argtypes = (GLuint, GLchar_p)  # program, name
glGetAttribLocation = gles2.glGetAttribLocation

""" GL_APICALL void         GL_APIENTRY glGetBufferParameteriv (GLenum target, GLenum pname, GLint* params); """
gles2.glGetBufferParameteriv.restype = None
gles2.glGetBufferParameteriv.argtypes = (GLenum, GLenum, GLint_p)  # target, pname, params
glGetBufferParameteriv = gles2.glGetBufferParameteriv

""" GL_APICALL void         GL_APIENTRY glGetIntegerv (GLenum pname, GLint* params); """
gles2.glGetIntegerv.restype = None
gles2.glGetIntegerv.argtypes = (GLenum, GLint_p)  # pname, params
glGetIntegerv = gles2.glGetIntegerv

""" GL_APICALL void         GL_APIENTRY glGetProgramiv (GLuint program, GLenum pname, GLint* params); """
gles2.glGetProgramiv.restype = None
gles2.glGetProgramiv.argtypes = (GLuint, GLenum, GLint_p)  # program, pname, params
glGetProgramiv = gles2.glGetProgramiv

""" GL_APICALL void         GL_APIENTRY glGetProgramInfoLog (GLuint program, GLsizei bufsize, GLsizei* length, GLchar* infolog); """
gles2.glGetProgramInfoLog.restype = None
gles2.glGetProgramInfoLog.argtypes = (GLuint, GLsizei, GLsizei_p, GLchar_p)  # program, bufsize, length, infolog
glGetProgramInfoLog = gles2.glGetProgramInfoLog

""" GL_APICALL void         GL_APIENTRY glGetShaderiv (GLuint shader, GLenum pname, GLint* params); """
gles2.glGetShaderiv.restype = None
gles2.glGetShaderiv.argtypes = (GLuint, GLenum, GLint_p)  # shader, pname, params
glGetShaderiv = gles2.glGetShaderiv

""" GL_APICALL void         GL_APIENTRY glGetShaderInfoLog (GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* infolog); """
gles2.glGetShaderInfoLog.restype = None
gles2.glGetShaderInfoLog.argtypes = (GLuint, GLsizei, GLsizei_p, GLchar_p)  # shader, bufsize, length, infolog
glGetShaderInfoLog = gles2.glGetShaderInfoLog

""" GL_APICALL void         GL_APIENTRY glGetShaderSource (GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* source); """
gles2.glGetShaderSource.restype = None
gles2.glGetShaderSource.argtypes = (GLuint, GLsizei, GLsizei_p, GLchar_p)  # shader, bufsize, length, source
glGetShaderSource = gles2.glGetShaderSource

""" GL_APICALL void         GL_APIENTRY glGetUniformfv (GLuint program, GLint location, GLfloat* params); """
gles2.glGetUniformfv.restype = None
gles2.glGetUniformfv.argtypes = (GLuint, GLint, GLfloat_p)  # program, location, params
glGetUniformfv = gles2.glGetUniformfv

""" GL_APICALL void         GL_APIENTRY glGetUniformiv (GLuint program, GLint location, GLint* params); """
gles2.glGetUniformiv.restype = None
gles2.glGetUniformiv.argtypes = (GLuint, GLint, GLint_p)  # program, location, params
glGetUniformiv = gles2.glGetUniformiv

""" GL_APICALL int          GL_APIENTRY glGetUniformLocation (GLuint program, const GLchar* name); """
gles2.glGetUniformLocation.restype = int
gles2.glGetUniformLocation.argtypes = (GLuint, GLchar_p)  # program, name
glGetUniformLocation = gles2.glGetUniformLocation

""" GL_APICALL void         GL_APIENTRY glGetVertexAttribiv (GLuint index, GLenum pname, GLint* params); """
gles2.glGetVertexAttribiv.restype = None
gles2.glGetVertexAttribiv.argtypes = (GLuint, GLenum, GLint_p)  # index, pname, params
glGetVertexAttribiv = gles2.glGetVertexAttribiv

""" GL_APICALL GLboolean    GL_APIENTRY glIsBuffer (GLuint buffer); """
gles2.glIsBuffer.restype = GLboolean
gles2.glIsBuffer.argtypes = (GLuint,)  # buffer
glIsBuffer = gles2.glIsBuffer

""" GL_APICALL GLboolean    GL_APIENTRY glIsProgram (GLuint program); """
gles2.glIsProgram.restype = GLboolean
gles2.glIsProgram.argtypes = (GLuint,)  # program
glIsProgram = gles2.glIsProgram

""" GL_APICALL GLboolean    GL_APIENTRY glIsShader (GLuint shader); """
gles2.glIsShader.restype = GLboolean
gles2.glIsShader.argtypes = (GLuint,)  # shader
glIsShader = gles2.glIsShader

""" GL_APICALL void         GL_APIENTRY glLinkProgram (GLuint program); """
gles2.glLinkProgram.restype = None
gles2.glLinkProgram.argtypes = (GLuint,)  # program
glLinkProgram = gles2.glLinkProgram

""" GL_APICALL void         GL_APIENTRY glShaderSource (GLuint shader, GLsizei count, const GLchar** string, const GLint* length); """
gles2.glShaderSource.restype = None
gles2.glShaderSource.argtypes = (GLuint, GLsizei, GLchar_p, GLint_p)  # shader, count, string, length
glShaderSource = gles2.glShaderSource

""" GL_APICALL void         GL_APIENTRY glUniform1fv (GLint location, GLsizei count, const GLfloat* v); """
gles2.glUniform1fv.restype = None
gles2.glUniform1fv.argtypes = (GLint, GLsizei, GLfloat_p)  # location, count, v
glUniform1fv = gles2.glUniform1fv

""" GL_APICALL void         GL_APIENTRY glUniform1iv (GLint location, GLsizei count, const GLint* v); """
gles2.glUniform1iv.restype = None
gles2.glUniform1iv.argtypes = (GLint, GLsizei, GLint_p)  # location, count, v
glUniform1iv = gles2.glUniform1iv

""" GL_APICALL void         GL_APIENTRY glUniform2fv (GLint location, GLsizei count, const GLfloat* v); """
gles2.glUniform2fv.restype = None
gles2.glUniform2fv.argtypes = (GLint, GLsizei, GLfloat_p)  # location, count, v
glUniform2fv = gles2.glUniform2fv

""" GL_APICALL void         GL_APIENTRY glUniform2iv (GLint location, GLsizei count, const GLint* v); """
gles2.glUniform2iv.restype = None
gles2.glUniform2iv.argtypes = (GLint, GLsizei, GLint_p)  # location, count, v
glUniform2iv = gles2.glUniform2iv

""" GL_APICALL void         GL_APIENTRY glUniform3fv (GLint location, GLsizei count, const GLfloat* v); """
gles2.glUniform3fv.restype = None
gles2.glUniform3fv.argtypes = (GLint, GLsizei, GLfloat_p)  # location, count, v
glUniform3fv = gles2.glUniform3fv

""" GL_APICALL void         GL_APIENTRY glUniform3iv (GLint location, GLsizei count, const GLint* v); """
gles2.glUniform3iv.restype = None
gles2.glUniform3iv.argtypes = (GLint, GLsizei, GLint_p)  # location, count, v
glUniform3iv = gles2.glUniform3iv

""" GL_APICALL void         GL_APIENTRY glUniform4fv (GLint location, GLsizei count, const GLfloat* v); """
gles2.glUniform4fv.restype = None
gles2.glUniform4fv.argtypes = (GLint, GLsizei, GLfloat_p)  # location, count, v
glUniform4fv = gles2.glUniform4fv

""" GL_APICALL void         GL_APIENTRY glUniform4iv (GLint location, GLsizei count, const GLint* v); """
gles2.glUniform4iv.restype = None
gles2.glUniform4iv.argtypes = (GLint, GLsizei, GLint_p)  # location, count, v
glUniform4iv = gles2.glUniform4iv

""" GL_APICALL void         GL_APIENTRY glUniformMatrix2fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value); """
gles2.glUniformMatrix2fv.restype = None
gles2.glUniformMatrix2fv.argtypes = (GLint, GLsizei, GLboolean, GLfloat_p)  # location, count, transpose, value
glUniformMatrix2fv = gles2.glUniformMatrix2fv

""" GL_APICALL void         GL_APIENTRY glUniformMatrix3fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value); """
gles2.glUniformMatrix3fv.restype = None
gles2.glUniformMatrix3fv.argtypes = (GLint, GLsizei, GLboolean, GLfloat_p)  # location, count, transpose, value
glUniformMatrix3fv = gles2.glUniformMatrix3fv

""" GL_APICALL void         GL_APIENTRY glUniformMatrix4fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value); """
gles2.glUniformMatrix4fv.restype = None
gles2.glUniformMatrix4fv.argtypes = (GLint, GLsizei, GLboolean, GLfloat_p)  # location, count, transpose, value
glUniformMatrix4fv = gles2.glUniformMatrix4fv

""" GL_APICALL void         GL_APIENTRY glUseProgram (GLuint program); """
gles2.glUseProgram.restype = None
gles2.glUseProgram.argtypes = (GLuint,)  # program
glUseProgram = gles2.glUseProgram

""" GL_APICALL void         GL_APIENTRY glVertexAttribPointer (GLuint indx, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const GLvoid* ptr); """
gles2.glVertexAttribPointer.restype = None
gles2.glVertexAttribPointer.argtypes = (GLuint, GLint, GLenum, GLboolean, GLsizei, GLvoid_p)  # indx, size, type, normalized, stride, ptr
glVertexAttribPointer = gles2.glVertexAttribPointer

""" GL_APICALL void         GL_APIENTRY glActiveTexture (GLenum texture); """
gles2.glActiveTexture.restype = None
gles2.glActiveTexture.argtypes = (GLenum,)  # texture
glActiveTexture = gles2.glActiveTexture

""" GL_APICALL void         GL_APIENTRY glBindTexture (GLenum target, GLuint texture); """
gles2.glBindTexture.restype = None
gles2.glBindTexture.argtypes = (GLenum, GLuint)  # target, texture
glBindTexture = gles2.glBindTexture

""" GL_APICALL void         GL_APIENTRY glEnable (GLenum cap); """
gles2.glEnable.restype = None
gles2.glEnable.argtypes = (GLenum,)  # cap
glEnable = gles2.glEnable
