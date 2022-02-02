#version 440

layout(location=0) in vec3 vertex_position;
layout(location=1) in vec3 in_color; // vertex color
out vec3 out_color;

void main() {
    gl_Position = vec4(vertex_position, 1);

    // return colors to fragment shader
    out_color = in_color;
}
