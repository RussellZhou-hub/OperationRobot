# image filename if there is a button image. GIFs and PNGs only.
import PySimpleGUI as sg

sg.theme('LightGreen')
# 窗体界面布局
layout = [
        [sg.Text('Image、FileBrowse演示', size=(40, 1), justification='center')],
        [sg.Text('操作结果：',k='-TEXT1-'),
         sg.FileBrowse("浏览",target='-GETFILE-',key='-GETFILE-',
         enable_events=True,font=16,size=(10,2))],
        [sg.Image(key="-IMAGE-",size=(300,200),filename=r'C:\Users\vincekzhou\Pictures\Saved Pictures\zhihu_article_cover.png')],
        [sg.Exit()],
    ]

# 窗体显示
window = sg.Window('PySimpleGUI Elements 测试', layout)

# 消息循环
while True:
    event, values = window.read()
    # print(event,values)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == '-GETFILE-':
        name = values['-GETFILE-']
        window['-TEXT1-'].update(name)
        window['-IMAGE-'].update(filename=name)
        window['-IMAGE-'].set_size(window['-IMAGE-'].get_size())

window.close()