namespace WinFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        static int gima(string str)
        {
            int sum = 0;
            string[] full = new string[] { "אלף", "בית", "גימל", "דלת", "הא", "ואו", "זין", "חית", "טת", "יוד", "כף", "למד", "מם", "נון", "סמך", "עין", "פה", "צדי", "קוף", "ריש", "שין", "תיו" };
            char[] let = new char[] { 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת', 'ך', 'ם', 'ן', 'ף', 'ץ' };
            int[] val = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 20, 40, 50, 80, 90 };
            for (int i = 0; i < str.Length; i++)
            {
                for (int j = 0; j < let.Length; j++)
                {
                    if (str[i] == let[j])
                    {
                        sum += val[j];
                    }

                }

            }


            return sum;

        }
        static int gimareco(string str, string f)
        {
            int d = int.Parse(f);
            int sum = 0;
            string[] full = new string[] { "אלף", "בית", "גימל", "דלת", "הא", "ואו", "זין", "חית", "טת", "יוד", "כף", "למד", "מם", "נון", "סמך", "עין", "פה", "צדי", "קוף", "ריש", "שין", "תיו", "כף", "מם", "נון", "פה", "צדי" };
            char[] let = new char[] { 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת', 'ך', 'ם', 'ן', 'ף', 'ץ' };
            int[] val = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 20, 40, 50, 80, 90 };
            if (d == 0)
            {

                for (int i = 0; i < str.Length; i++)
                {
                    for (int j = 0; j < let.Length; j++)
                    {
                        if (str[i] == let[j])
                        {
                            sum += val[j];
                        }

                    }

                }


                return sum;
            }
            else
            {
                sum = 0;
                for (int i = 0; i < str.Length; i++)
                {
                    for (int j = 0; j < let.Length; j++)
                    {
                        if (str[i] == let[j])
                        {
                            sum += gimareco(full[j], (d - 1).ToString());
                        }
                    }
                }
                return sum;
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("esdgfdg");
        }

        private void button2_Click(object sender, EventArgs e)
        {

            int a = gimareco(textBox1.Text, textBox2.Text);
            MessageBox.Show(a.ToString());

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {


        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            int a = gimareco(textBox1.Text, textBox2.Text);
            MessageBox.Show(a.ToString());
        }
    }
}
