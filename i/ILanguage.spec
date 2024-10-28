Summary: An interpreter for a J-inspired language
Name: ILanguage
Version: 0.1
Release: 1
License: ISC
Group: Development/Languages
Source0: %{name}-master.zip
URL: https://github.com/mlochbaum/ILanguage

%description
I is a language which generalizes the array and functional capabilities of
the array-programming language J to deal with a much broader variety of
data structures.

%prep
%setup -q -n %{name}-master

%build
gcc *.c -g -O -Wl,--allow-multiple-definition -o I

%install
install -Dm755 I %{buildroot}%{_bindir}/I

%files 
%doc LICENSE README.md doc examples ic
%{_bindir}/I

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
