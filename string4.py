#!/usr/bin/env python3
#positional formatting
print('to {}. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the {}, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived apple not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It {} computer was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with {} desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'.format('syou', 12, 'syou', 'syou'))

#Named placeholder
print('to {name}. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the {age:d}, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived apple not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It {name} computer was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with {age} desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'.format(name='syou', age=12))
