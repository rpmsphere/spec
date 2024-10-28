Summary: Screen Editor
Name: se
Version: 3.0.1
Release: 4.1
License: GPL
Group: Applications/Editors
Source: https://se-editor.org/dist/%{name}-%{version}.tar.gz
URL: https://se-editor.org/
BuildRequires: gcc-c++, ncurses

%description
se is a screen oriented version of the classic UNIX text editor ed.
Features:
* command syntax that is very familiar to users who already know ed.
* full visual interface allowing you to see the text you’re editing.
* built-in help system which describes many of the available commands.
* many configurable options which can be loaded from a .serc file.
* can be run interactively or in a script via the included scriptse utility.
* portable across many platforms.
* will notify you if you have new/unread e-mail.
* optional usage logging.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install
mv %{buildroot}%{_bindir}/se %{buildroot}%{_bindir}/se-editor

%files
%doc COPYING README ChangeLog TODO NEWS
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/man/man1/*

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.1
- Rebuilt for Fedora
