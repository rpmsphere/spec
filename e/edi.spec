%undefine _debugsource_packages

Name: edi
Version: 1.1
Release: 4.1
Summary: An Interactive Editor for Linux
License: GPLv2
Group: Applications/Editors
URL: http://edi.sourceforge.net/
Source0: http://sourceforge.net/projects/edi/files/edi-src/version%{version}/edi%{version}.tar.gz

%description
Edi is an interactive text based GUI Editor for Linux. It has C/C++ syntax
highlighting, a rich set of menus, multiple window support and much more.
It is mainly aimed at making people more comfortable with the Linux environment.
This editor avoids the need for a new Linux user to learn the VI editor's
not-so-friendly user interface.

%prep
%setup -q -n src
sed -i '/new\.h/d' linkstd.C

%build
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README
%{_bindir}/%{name}

%changelog
* Fri Feb 07 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
