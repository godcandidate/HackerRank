#include <iostream>
#include <sstream>
using namespace std;

/**
 * The Student class represents a student's details, including their age,
 * first name, last name, and standard.
 */
class Student
{
    private:
        int age;
        string first_name;
        string last_name;
        int standard;

    public:
        int get_age()
        {
            return age;
        }
        void set_age(int d)
        {
            age = d;
        }
        string get_first_name()
        {
            return first_name;
        }
        void set_first_name(string firstname)
        {
            first_name = firstname;
        }
        string get_last_name()
        {
            return last_name;
        }
        void set_last_name(string lastname)
        {
            last_name = lastname;
        }
        int get_standard()
        {
            return standard;
        }
        void set_standard(int stand)
        {
            standard = stand;
        }
        string to_string()
        {
           stringstream ss;
        ss << age << "," << first_name << "," << last_name << "," << standard;
        return ss.str();
        }


};

// HackerRank's int main, no changes
int main() {
    int age, standard;
    string first_name, last_name;

    cin >> age >> first_name >> last_name >> standard;

    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);

    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();

    return 0;
}

