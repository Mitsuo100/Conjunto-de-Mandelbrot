# Conjunto de Mandelbrot

Implementação do **Conjunto de Mandelbrot** em Python, utilizando números complexos, NumPy e Matplotlib para gerar uma visualização gráfica do fractal.

O projeto aplica iterativamente a sequência:

**zₙ₊₁ = zₙ² + c**

Para cada ponto `c` do plano complexo, o programa inicia `z` em `0` e verifica seu comportamento ao longo das iterações. Quando o módulo de `z` ultrapassa `2`, o ponto é considerado como tendo escapado.

A quantidade de iterações necessárias para cada ponto é utilizada para gerar a coloração da imagem, resultando na representação visual característica do Mandelbrot.

## Tecnologias

- Python
- NumPy
- Matplotlib
- Números complexos

## Conceitos explorados

- Fractais
- Números complexos
- Iterações matemáticas
- Visualização de dados
- Matrizes e processamento numérico
- Geração de imagens com Matplotlib