using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using LiveCharts;

using LiveCharts.Wpf;

namespace Lab1
{
    internal static class Program
    {
        /// <summary>
        /// Главная точка входа для приложения.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
            CartesianChart cartesianChart1 = new CartesianChart();
            cartesianChart1.Series = new SeriesCollection
            {
                new ColumnSeries
                {
                    Title = "Frequencies",
                    Values = new ChartValues<int> { 10, 15, 7, 22, 18 }, // Replace with your frequency data
                }
            };
        }
    }
}
