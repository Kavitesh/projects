Sub FormatTable()
    Dim ws As Worksheet
    Dim tblRange As Range

    ' Set worksheet
    Set ws = ActiveSheet

    ' Define the range to format (assumes data starts at A1 and goes until first empty row/column)
    Set tblRange = ws.Range("A1").CurrentRegion

    ' Make headers bold
    tblRange.Rows(1).Font.Bold = True

    ' Auto-fit columns
    tblRange.Columns.AutoFit

    ' Add borders around all cells
    With tblRange.Borders
        .LineStyle = xlContinuous
        .Color = vbBlack
        .Weight = xlThin
    End With

    ' Shade the header row light gray
    tblRange.Rows(1).Interior.Color = RGB(220, 220, 220)

    MsgBox "Table formatted successfully!"
End Sub
