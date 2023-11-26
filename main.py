import flet as ft
from CompressPDF import CompressPDF
from MergePDF import MergePDF
from PDF2DDOCX import PDF2DOCX
import webbrowser

def main(page: ft.Page):
    index=0    
    
    def changetab(e):
        nonlocal index
        index=my_index=e.control.selected_index
        file_names.value=None
        
        tab_1.visible=True if my_index==0 else False
        compbtn.visible=True if my_index==0 else False
        compratio.visible=True if my_index==0 else False
        
        tab_2.visible=True if my_index==1 else False
        mergebtn.visible=True if my_index==1 else False
        
        tab_3.visible=True if my_index==2 else False
        convertpdfbtn.visible=True if my_index==2 else False
        page.update()

        
    def file_Picker_Result(e:ft.FilePickerResultEvent):
        nonlocal index
        if index==0 :        
            compbtn.disabled=False if e.files is not None else True
            compratio.disabled=False if e.files is not None and compratio.value is not None else True
            page.update()
            file_names.value=(
            " , ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!" )
            file_names.update()
            page.update()
            compbtn.on_click=(lambda _:compress(e.files[0].path,int(compratio.value),e,e.files[0].name))
            page.update()
            compbtn.disabled=True
            
        if index==1:
            mergebtn.disabled=False if e.files is not None else True
            page.update()
            file_names.value=(
            " , ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!" )
            file_names.update()
            paths=[]
            for i in e.files:
                paths.append(i.path)
            mergebtn.on_click=(lambda _:merge(paths,e))
            page.update()
            mergebtn.disabled=True
           
        if index==2:
            convertpdfbtn.disabled=False if e.files is not None else True
            page.update()
            file_names.value=(
            " , ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!" )
            file_names.update()
            page.update()
            convertpdfbtn.on_click=(lambda _:pdf2docx(e.files[0].path,e,e.files[0].name))
            page.update()
            convertpdfbtn.disabled=True
            
    def compress(Path:str,quality,e,name):
        c=CompressPDF()
        currentprocess.value="PDF is being Compressed"
        currentprocess.visible=True
        tab_1.visible=False
        compbtn.visible=False
        progring.visible=True
        compratio.visible=False
        page.navigation_bar.visible=False
        file_names.visible=False
        progring.tooltip="Your PDF is Being Compressed"
        page.update()
        c.compressPDF(Path,quality,name)
        tab_1.visible=True
        compbtn.visible=True
        progring.visible=False
        currentprocess.value=None
        currentprocess.visible=False
        compratio.visible=True
        page.navigation_bar.visible=True
        file_names.visible=True
        e.files=None
        file_names.value=None
        page.update()
        snackbartext.value="PDF Compressed Successfully"
        snackbartext.text_align='center'
        openSnackbar()
    
    def merge(paths:list,e):
        m=MergePDF()
        currentprocess.value="PDF is being Merged"
        currentprocess.visible=True
        tab_2.visible=False
        mergebtn.visible=False
        progring.visible=True
        page.navigation_bar.visible=False
        file_names.visible=False
        progring.tooltip="Your PDF is Being Merged"
        page.update()
        m.merge_pdfs(paths)
        tab_2.visible=True
        mergebtn.visible=True
        progring.visible=False
        currentprocess.value=None
        currentprocess.visible=False
        page.navigation_bar.visible=True
        file_names.visible=True
        e.files=None
        file_names.value=None
        page.update()
        snackbartext.value="PDF Merged Successfully"
        snackbartext.text_align='center'
        openSnackbar()
    
    def pdf2docx(Path,e,name):
        p=PDF2DOCX()
        tab_3.visible=False
        convertpdfbtn.visible=False
        currentprocess.value="PDF is being Converted to DOCX"
        currentprocess.visible=True
        progring.visible=True
        page.navigation_bar.visible=False
        file_names.visible=False
        progring.tooltip="Your PDF is Being Merged"
        page.update()
        p.convert_pdf_to_docx(Path,name)
        tab_3.visible=True
        convertpdfbtn.visible=True
        progring.visible=False
        currentprocess.value=None
        currentprocess.visible=False
        page.navigation_bar.visible=True
        file_names.visible=True
        e.files=None
        file_names.value=None
        page.update()
        snackbartext.value="PDF Converted to DOCX Successfully"
        snackbartext.text_align='center'
        openSnackbar()

    def on_compbtn_text_changed(e):
        try:
            value = int(e.control.value)
        except ValueError:
            value = None
            compbtn.disabled=True
                
        if value is None or value < 0 or value > 99:
            e.control.value = None
            compbtn.disabled=True
        else:
            e.control.value = str(value)
            compbtn.disabled=False
        page.update()
        
    def openSnackbar():
        page.snack_bar = ft.SnackBar(snackbartext,bgcolor='#FC8955')
        page.snack_bar.open = True
        page.update()
        
    def open_github(e):
        webbrowser.open_new_tab('https://github.com/TheMtyHulk/PDF-processing-app.git')

    page.title = "Pdf Procesing Tool"
    filepicker=ft.FilePicker(on_result=file_Picker_Result)
    page.controls.append(filepicker)
    
    
    page.navigation_bar = ft.NavigationBar(
        bgcolor="#0583D2",
        on_change=changetab,
        selected_index=0,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.COMPRESS_OUTLINED,selected_icon=ft.icons.COMPRESS, label="COMPRESS"),
            ft.NavigationDestination(icon=ft.icons.MERGE_OUTLINED,selected_icon=ft.icons.MERGE, label="MERGE",),
            ft.NavigationDestination(
                icon=ft.icons.CHANGE_CIRCLE_OUTLINED,
                selected_icon=ft.icons.CHANGE_CIRCLE,
                label="PDF 2 DOCX" ),
        ]
    )
    page.appbar = ft.AppBar(
        leading=ft.Image(src='Myself 2023edited.png',width=30,height=30,border_radius=100),
        leading_width=50,
        title=ft.Text("Developed by: Pramod J"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text='GITHUB',on_click=open_github),
                   
                    
                ]
            ),
        ],
    )
    tab_1=(
        ft.Container(
            content=ft.Text("select your files",size=15,color=ft.colors.BLACK,font_family="Ariel",text_align="center"),
            width=180,
            height=180,
            bgcolor='#00FFEF',
            alignment=ft.alignment.center,
            padding=10,
            margin=10,
            ink=True,
            border_radius=40,
            on_click=lambda e:filepicker.pick_files(allow_multiple=False,file_type=ft.FilePickerFileType.CUSTOM,allowed_extensions=["pdf"])
            )
        )

    tab_2=(
        ft.Container(
            content=ft.Text("select your files",size=15,color=ft.colors.BLACK,font_family="Ariel",text_align="center"),
            width=180,
            height=180,
            bgcolor='#00FFEF',
            alignment=ft.alignment.center,
            padding=10,
            margin=10,
            ink=True,
            border_radius=40,
            on_click=lambda e:filepicker.pick_files(allow_multiple=True,file_type=ft.FilePickerFileType.CUSTOM,allowed_extensions=["pdf"]),
            visible=False
            )
        )
 
    tab_3=(
        ft.Container(
            content=ft.Text("select your files",size=15,color=ft.colors.BLACK,font_family="Ariel",text_align="center"),
            width=180,
            height=180,
            bgcolor='#00FFEF',
            alignment=ft.alignment.center,
            padding=10,
            margin=10,
            ink=True,
            border_radius=40,
            on_click=lambda e:filepicker.pick_files(allow_multiple=False,file_type=ft.FilePickerFileType.CUSTOM,allowed_extensions=["pdf"]),
            visible=False
            )
        )
    
    file_names=ft.Text()
    currentprocess=ft.Text(size=30,visible=False)
    compratio=ft.TextField(on_change=on_compbtn_text_changed,label='compression ratio',value=30,width=130,hint_text="In Percentage",disabled=True)
    mergebtn=ft.ElevatedButton(text="MERGE",disabled=True,width=200,height=70,visible=False)
    convertpdfbtn=ft.ElevatedButton(text="CONVERT",disabled=True,width=200,height=70,visible=False)
    compbtn=ft.ElevatedButton(text="COMPRESS",disabled=True,width=200,height=70)
    progring=ft.ProgressRing(visible=False)
    snackbartext=ft.Text()
    page.snack_bar = ft.SnackBar(
        content=snackbartext,
        action="Alright!",
    )
    
    view = ft.Column(
        
        #width=800,
        controls=[
            ft.Row(
                controls=[
                    
                    tab_1,
                    tab_2,
                    tab_3,
                    compratio,
                    
                ],
                   
                alignment=ft.MainAxisAlignment.CENTER,
            ),
             ft.Column(controls=[ft.Row(controls=[file_names,progring],alignment=ft.MainAxisAlignment.CENTER)]),
            ft.Column(controls=[ft.Row(controls=[compbtn,mergebtn,convertpdfbtn,currentprocess],alignment=ft.MainAxisAlignment.CENTER)]),
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        
    )
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.add(view)
    page.update()


ft.app(target=main)