Name: kabikaboo
Summary: Recursive Writing Assistant
Version: 1.7
Release: 5.1
Group: Applications/Publishing
License: GPL
URL: https://launchpad.net/kabikaboo
Source0: https://launchpadlibrarian.net/37092984/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: pygtk2
Requires: gnome-python2-gtkspell

%description
Kabikaboo is a tree-based note pad, designed to help you plan a book or complex
project. Kabikaboo aims to make the author's life easier by providing a way to
edit and organize a collection of related text files. The program can be used
to plan a series of books, technical manuals, software projects, or anything
that would benefit from tree-based text organization.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 man/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a help src ui %{name}.png $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/help/%{name}
cp -a help/C $RPM_BUILD_ROOT%{_datadir}/gnome/help/%{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/src/kabikaboo.py
sed -i 's|^python |python2 |' $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc COPYING*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Nov 04 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
