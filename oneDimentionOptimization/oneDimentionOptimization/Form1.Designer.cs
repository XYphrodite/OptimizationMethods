namespace oneDimentionOptimization
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.Series series2 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.SymbolOfVariableTextBox = new System.Windows.Forms.TextBox();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.FunctionTextBox = new System.Windows.Forms.TextBox();
            this.a0TextBox = new System.Windows.Forms.TextBox();
            this.StatusRichTextBox = new System.Windows.Forms.RichTextBox();
            this.SymbolOfVariableLabel = new System.Windows.Forms.Label();
            this.FunctionLabel = new System.Windows.Forms.Label();
            this.a0Label = new System.Windows.Forms.Label();
            this.b0Label = new System.Windows.Forms.Label();
            this.b0TextBox = new System.Windows.Forms.TextBox();
            this.StatusBarLabel = new System.Windows.Forms.Label();
            this.ResultLabel = new System.Windows.Forms.Label();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.CalculateButton = new System.Windows.Forms.Button();
            this.radioButton1 = new System.Windows.Forms.RadioButton();
            this.radioButton2 = new System.Windows.Forms.RadioButton();
            this.radioButton3 = new System.Windows.Forms.RadioButton();
            this.label1 = new System.Windows.Forms.Label();
            this.EtextBox = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            this.SuspendLayout();
            // 
            // SymbolOfVariableTextBox
            // 
            this.SymbolOfVariableTextBox.Location = new System.Drawing.Point(89, 9);
            this.SymbolOfVariableTextBox.Name = "SymbolOfVariableTextBox";
            this.SymbolOfVariableTextBox.Size = new System.Drawing.Size(24, 20);
            this.SymbolOfVariableTextBox.TabIndex = 0;
            // 
            // FunctionTextBox
            // 
            this.FunctionTextBox.Location = new System.Drawing.Point(89, 35);
            this.FunctionTextBox.Name = "FunctionTextBox";
            this.FunctionTextBox.Size = new System.Drawing.Size(100, 20);
            this.FunctionTextBox.TabIndex = 1;
            // 
            // a0TextBox
            // 
            this.a0TextBox.Location = new System.Drawing.Point(89, 61);
            this.a0TextBox.Name = "a0TextBox";
            this.a0TextBox.Size = new System.Drawing.Size(100, 20);
            this.a0TextBox.TabIndex = 2;
            // 
            // StatusRichTextBox
            // 
            this.StatusRichTextBox.Location = new System.Drawing.Point(12, 464);
            this.StatusRichTextBox.Name = "StatusRichTextBox";
            this.StatusRichTextBox.Size = new System.Drawing.Size(1224, 109);
            this.StatusRichTextBox.TabIndex = 3;
            this.StatusRichTextBox.Text = "";
            // 
            // SymbolOfVariableLabel
            // 
            this.SymbolOfVariableLabel.AutoSize = true;
            this.SymbolOfVariableLabel.Location = new System.Drawing.Point(12, 16);
            this.SymbolOfVariableLabel.Name = "SymbolOfVariableLabel";
            this.SymbolOfVariableLabel.Size = new System.Drawing.Size(71, 13);
            this.SymbolOfVariableLabel.TabIndex = 4;
            this.SymbolOfVariableLabel.Text = "Переменная";
            // 
            // FunctionLabel
            // 
            this.FunctionLabel.AutoSize = true;
            this.FunctionLabel.Location = new System.Drawing.Point(12, 42);
            this.FunctionLabel.Name = "FunctionLabel";
            this.FunctionLabel.Size = new System.Drawing.Size(53, 13);
            this.FunctionLabel.TabIndex = 5;
            this.FunctionLabel.Text = "Функция";
            // 
            // a0Label
            // 
            this.a0Label.AutoSize = true;
            this.a0Label.Location = new System.Drawing.Point(12, 68);
            this.a0Label.Name = "a0Label";
            this.a0Label.Size = new System.Drawing.Size(19, 13);
            this.a0Label.TabIndex = 6;
            this.a0Label.Text = "a0";
            // 
            // b0Label
            // 
            this.b0Label.AutoSize = true;
            this.b0Label.Location = new System.Drawing.Point(12, 94);
            this.b0Label.Name = "b0Label";
            this.b0Label.Size = new System.Drawing.Size(19, 13);
            this.b0Label.TabIndex = 7;
            this.b0Label.Text = "b0";
            // 
            // b0TextBox
            // 
            this.b0TextBox.Location = new System.Drawing.Point(89, 87);
            this.b0TextBox.Name = "b0TextBox";
            this.b0TextBox.Size = new System.Drawing.Size(100, 20);
            this.b0TextBox.TabIndex = 8;
            // 
            // StatusBarLabel
            // 
            this.StatusBarLabel.AutoSize = true;
            this.StatusBarLabel.Location = new System.Drawing.Point(12, 448);
            this.StatusBarLabel.Name = "StatusBarLabel";
            this.StatusBarLabel.Size = new System.Drawing.Size(99, 13);
            this.StatusBarLabel.TabIndex = 9;
            this.StatusBarLabel.Text = "Строка состояния";
            // 
            // ResultLabel
            // 
            this.ResultLabel.AutoSize = true;
            this.ResultLabel.Location = new System.Drawing.Point(12, 262);
            this.ResultLabel.Name = "ResultLabel";
            this.ResultLabel.Size = new System.Drawing.Size(71, 13);
            this.ResultLabel.TabIndex = 10;
            this.ResultLabel.Text = "Результат: —";
            // 
            // chart1
            // 
            chartArea1.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chart1.Legends.Add(legend1);
            this.chart1.Location = new System.Drawing.Point(225, 12);
            this.chart1.Name = "chart1";
            series1.BorderWidth = 4;
            series1.ChartArea = "ChartArea1";
            series1.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Point;
            series1.Color = System.Drawing.Color.Red;
            series1.Legend = "Legend1";
            series1.LegendText = "f(x)";
            series1.Name = "Series1";
            series2.BorderWidth = 2;
            series2.ChartArea = "ChartArea1";
            series2.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Spline;
            series2.Legend = "Legend1";
            series2.LegendText = "f(x)";
            series2.Name = "Series2";
            this.chart1.Series.Add(series1);
            this.chart1.Series.Add(series2);
            this.chart1.Size = new System.Drawing.Size(1011, 446);
            this.chart1.TabIndex = 11;
            this.chart1.Text = "chart1";
            // 
            // CalculateButton
            // 
            this.CalculateButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.CalculateButton.Location = new System.Drawing.Point(15, 134);
            this.CalculateButton.Name = "CalculateButton";
            this.CalculateButton.Size = new System.Drawing.Size(174, 23);
            this.CalculateButton.TabIndex = 13;
            this.CalculateButton.Text = "Calculate";
            this.CalculateButton.UseVisualStyleBackColor = true;
            this.CalculateButton.Click += new System.EventHandler(this.CalculateButton_Click);
            // 
            // radioButton1
            // 
            this.radioButton1.AutoSize = true;
            this.radioButton1.Location = new System.Drawing.Point(15, 163);
            this.radioButton1.Name = "radioButton1";
            this.radioButton1.Size = new System.Drawing.Size(137, 17);
            this.radioButton1.TabIndex = 14;
            this.radioButton1.TabStop = true;
            this.radioButton1.Text = "Половинного деления";
            this.radioButton1.UseVisualStyleBackColor = true;
            // 
            // radioButton2
            // 
            this.radioButton2.AutoSize = true;
            this.radioButton2.Location = new System.Drawing.Point(15, 187);
            this.radioButton2.Name = "radioButton2";
            this.radioButton2.Size = new System.Drawing.Size(126, 17);
            this.radioButton2.TabIndex = 15;
            this.radioButton2.TabStop = true;
            this.radioButton2.Text = "\"Золотого\" сечения";
            this.radioButton2.UseVisualStyleBackColor = true;
            // 
            // radioButton3
            // 
            this.radioButton3.AutoSize = true;
            this.radioButton3.Location = new System.Drawing.Point(15, 211);
            this.radioButton3.Name = "radioButton3";
            this.radioButton3.Size = new System.Drawing.Size(82, 17);
            this.radioButton3.TabIndex = 16;
            this.radioButton3.TabStop = true;
            this.radioButton3.Text = "Фибоначчи";
            this.radioButton3.UseVisualStyleBackColor = true;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(119, 16);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(14, 13);
            this.label1.TabIndex = 17;
            this.label1.Text = "E";
            // 
            // EtextBox
            // 
            this.EtextBox.Location = new System.Drawing.Point(139, 9);
            this.EtextBox.Name = "EtextBox";
            this.EtextBox.Size = new System.Drawing.Size(50, 20);
            this.EtextBox.TabIndex = 18;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Info;
            this.ClientSize = new System.Drawing.Size(1248, 585);
            this.Controls.Add(this.EtextBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.radioButton3);
            this.Controls.Add(this.radioButton2);
            this.Controls.Add(this.radioButton1);
            this.Controls.Add(this.CalculateButton);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.ResultLabel);
            this.Controls.Add(this.StatusBarLabel);
            this.Controls.Add(this.b0TextBox);
            this.Controls.Add(this.b0Label);
            this.Controls.Add(this.a0Label);
            this.Controls.Add(this.FunctionLabel);
            this.Controls.Add(this.SymbolOfVariableLabel);
            this.Controls.Add(this.StatusRichTextBox);
            this.Controls.Add(this.a0TextBox);
            this.Controls.Add(this.FunctionTextBox);
            this.Controls.Add(this.SymbolOfVariableTextBox);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox SymbolOfVariableTextBox;
        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.TextBox FunctionTextBox;
        private System.Windows.Forms.TextBox a0TextBox;
        private System.Windows.Forms.RichTextBox StatusRichTextBox;
        private System.Windows.Forms.Label SymbolOfVariableLabel;
        private System.Windows.Forms.Label FunctionLabel;
        private System.Windows.Forms.Label a0Label;
        private System.Windows.Forms.Label b0Label;
        private System.Windows.Forms.TextBox b0TextBox;
        private System.Windows.Forms.Label StatusBarLabel;
        private System.Windows.Forms.Label ResultLabel;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.Button CalculateButton;
        private System.Windows.Forms.RadioButton radioButton1;
        private System.Windows.Forms.RadioButton radioButton2;
        private System.Windows.Forms.RadioButton radioButton3;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox EtextBox;
    }
}

