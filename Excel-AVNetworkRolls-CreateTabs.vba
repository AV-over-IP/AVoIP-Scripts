' Version: 1.0
' Author: carlos.soto@trisonworld.com
' Date: 07/09/2023
' Description: Este script crea y/o renombra pestañas en el Libro Rolls Royce Network assignment
'              basándose en los valores de la columna B de la hoja activa. ( Rolls Dealers )
'              las nuevas pestañas estarán formateadas con la plantilla de la Plantilla super-oculta.

Sub CreateTabs()
    ' Declaración de variables
    Dim newWs As Worksheet
    Dim mainWs As Worksheet
    Dim templateWs As Worksheet
    Dim currentCell As Range
    Dim sheetName As String
    Dim sheetExists As Boolean
    Dim i As Long
    Dim col As Integer
    
    ' Hojas de trabajo
    Set mainWs = ActiveSheet
    Set templateWs = ThisWorkbook.Sheets("Plantilla")
    
    ' Bucle para recorrer proyectos
    For i = 9 To 401 Step 2 ' Usamos índices impares ya que estas filas al tener 2 rangos de IP ocupan 2 filas
    
        Set currentCell = mainWs.Cells(i, 2) ' Celda de iteración
        
        ' Salimos del bucle si hemos acabado los proyectos que tenemos disponibles
        If IsEmpty(currentCell.Value) Or InStr(1, currentCell.Value, "DEALERSHIP", vbTextCompare) > 0 Then Exit For
        
        ' Verificamos si ya existe hoja para el proyecto de la iteración actual
        sheetName = currentCell.Value
        sheetExists = False
        For Each newWs In ThisWorkbook.Sheets
            If newWs.Name = sheetName Then
                sheetExists = True
                Exit For
            End If
        Next newWs
        
        ' En caso de que no exista hoja, la creamos
        If Not sheetExists Then

            Set newWs = ThisWorkbook.Sheets.Add(After:=ThisWorkbook.Sheets(ThisWorkbook.Sheets.Count))
            newWs.Name = sheetName
            
            ' Copiamos la plantilla a la nueva hoja
            templateWs.Range("A1:Z100").Copy Destination:=newWs.Range("A1")
            
            ' Y ajustamos los anchos de columna para una mejor visibilidad
            For col = 1 To 26
            
                newWs.Columns(col).ColumnWidth = templateWs.Columns(col).ColumnWidth
                
            Next col
            
        End If
        
    Next i
        
End Sub

