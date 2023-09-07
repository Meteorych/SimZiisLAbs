using Lab1AOIS;
using LiveCharts.Wpf;
using LiveCharts;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lab1
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
            textBoxLength.Text = $"Input the Length:{Environment.NewLine}";
        }
        
        private void button1_Click(object sender, EventArgs e)
        {
            
            textBoxOutput.Clear();
            
            try
            {
                int length = int.Parse(textBoxLength.Lines[1]);

                //Generate the password
                Password password = new Password(length);

                //Display the generated password
                DisplayPasswordDistribution(password.GetPassword);
                textBoxOutput.Text = $"Generated password: {password.GetPassword}{Environment.NewLine}Average time of brutforce:{password.BrutForceTime()} ms";
                
            }
            catch (FormatException)
            {
                textBoxOutput.AppendText("\nPlease enter a valid numeric length.");
            }
        }
        private void DisplayPasswordDistribution(string password)
        {
            SeriesCollection seriesCollection = new SeriesCollection();

            foreach (char c in password)
            {
                int count = password.Count(ch => ch == c);
                seriesCollection.Add(new ColumnSeries
                {
                    Title = c.ToString(),
                    Values = new ChartValues<int> { count }
                });
            }

            cartesianChart1.Series = seriesCollection;
        }
    }
}

