Name: optiman
Summary: A small utility to transform man pages
Version: 1.1.1
Release: 3.1
Group: Development/Tools
URL: http://lav.yar.ru/programs.html
Source0: http://ftp.yar.ru/pub/source/misc/%{name}-%{version}.tgz
License: Public Domain
BuildRequires: ncurses-devel

%description
Optimizes formatted by nroff man pages by changing many BS to one CR. Speeds up
printing a lot (at least on plain matrix printers). It can also use printer
capabilities for italic and bold fonts. Terminfo for Epson printer included.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README
%{_bindir}/%{name}

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuilt for Fedora
