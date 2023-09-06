using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1AOIS
{
    internal class Password
    {
        private string _password;
        private const string valid = "абвгдеёжзийклмнпрстоуфхцчщшъыьэюя0123456789";
        public Password(int length)
        {
            Random random = new Random();
            StringBuilder buildPassword = new StringBuilder();
            while (0 < length--)
            {
                buildPassword.Append(valid[random.Next(valid.Length)]);
            }
            _password = buildPassword.ToString();
            Console.WriteLine(_password);
        }
    }

}
