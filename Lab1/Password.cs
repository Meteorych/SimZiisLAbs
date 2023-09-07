using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace Lab1AOIS
{
    internal class Password
    {
        private string _password;
        private int _length;
        private const string _valid = "абвгдеёжзийклмнпрстоуфхцчщшъыьэюя0123456789";
        public Password(int length)
        {
            
            _length = length;
            _password = BuildPassword();
        }
        /// <summary>
        /// Generating random password
        /// </summary>
        /// <returns></returns>
        public string BuildPassword()
        {
            Random random = new Random();
            StringBuilder buildPassword = new StringBuilder();

            for (int i = 0; i < _length; i++)
            {
                buildPassword.Append(_valid[random.Next(_valid.Length)]);
            }
            return buildPassword.ToString();
        }

        public string GetPassword { get { return _password; } }

        public long BrutForceTime()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            
            for(int i = 0; i <= 5; i++)
            {
                BrutForce();
                _password = BuildPassword();
            }
            
            sw.Stop();
            Console.WriteLine(sw.ElapsedMilliseconds / 5);
            return sw.ElapsedMilliseconds/5;
        }
        private void BrutForce()
        {
            char[] password = new char[_length];
            for (int i = 0; i < _length; i++)
            {
                password[i] = _valid[0];
            }

            while (true)
            {
                for (int i = _length - 1; i >= 0; i--)
                {
                    string password2 = new string(password);
                    if (password2 == _password)
                    {
                        return;
                    }
                    if (password[i] == _valid.Last())
                    {
    
                        password[i] = _valid[0];
                    }
                    else
                    {
                        password[i] = _valid[_valid.IndexOf(password[i]) + 1];
                        break;
                    }
                }
            }
        }
    }

}
