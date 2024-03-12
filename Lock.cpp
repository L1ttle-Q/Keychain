#include <cstdio>
#include <iostream>

using namespace std;

namespace _rand
{
    const int mod = 4953;
    int seed = 5055;

    void Srand(int a)
    {
        seed = a % mod;
    }

    int Rand()
    {
        seed = (((((seed << 7) - 1053) % mod * seed - 2753) * 31) % mod + mod) % mod;
        return 55 + seed % 30;
    }
}

int Hash(string s)
{
    const int mod = 4971;
    int H = 0, len = s.length();
    for (int i = 0; i < len; i++)
        H = (H + (((s[i] + 115) << 3) % mod * s[i] - 2334) % mod + mod) % mod;
    return H;
}

string Rev(string s)
{
    string t;
    for (int i = s.length() - 1; i >= 0; i--)
        t += s[i];
    return t;
}

int P(char a)
{
    if (a % 2)
        return 1;
    return -1;
}

const int L = 16;
string s, key;
int main(int argc, char* argv[])
{
    s = string(argv[1]);
    int opt(atoi(argv[2]));
                            //opt: 1 for lock
                            //opt: -1 for unlock
    int sd, ver;
    char ss[6];

    if (opt == 1)
    {
        sd = Hash(s);
        _rand::Srand(sd);

        //generate key and write in the file
        for (int i = 0; i < L; i++)
            key += 79 + _rand::Rand() * P(s[i * 353 % s.length()]);

        ver = Hash(key);
        sprintf(ss, "%05d", ver);
        for (int i = 0; i < 5; i++)
            s += ss[i];

        s = Rev(s);
    }
    if (opt == -1)
    {
        char c;
        s.clear();key.clear();
        freopen("key.txt", "r", stdin);
        while (scanf("%c", &c) != EOF)
            s += c;
        fclose(stdin);

        freopen("sec.txt", "r", stdin);
        if (scanf("%d\n", &sd) == EOF)
        {
            fclose(stdin);
            cout << "---";
            return 0;
        }
        while (scanf("%c", &c) != EOF)
            key += c;
        fclose(stdin);

        _rand::Srand(sd * 5 + 33577);
        for (int i = 0; i < L; i++)
            key[i] ^= _rand::Rand();
    }

    int len = s.length();

    for (int i = 0; i < len; i += L)
        for (int j = 0; j < L && i + j < len; j++)
                s[i + j] ^= key[j];

    if (opt == 1)
    {
        _rand::Srand(sd * 5 + 33577);
        for (int i = 0; i < L; i++)
            key[i] ^= _rand::Rand();

        freopen("sec.txt", "w", stdout);
        cout << sd << endl << key;
        fclose(stdout);

        freopen("key.txt", "w", stdout);
        cout << s;
        fclose(stdout);
    }

    if (opt == -1)
    {
        s = Rev(s);
        ver = 0;
        for (int i = 5; i >= 1; i--)
            ver = ver * 10 + s[s.length() - i] - '0';

        if (ver != Hash(key))
            s = "---";
        else
            s = s.substr(0, s.length() - 5);

        cout << s;
    }
    return 0;
}