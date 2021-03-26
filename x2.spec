Summary: An micro-ide/text editor written in C/GTK+
Name: x2
Version: 1.1.0
Release: 7.1
License: BSD
Group: Applications/Editors
URL: http://gtk-apps.org/content/show.php/X2?content=145463
Source: http://gtk-apps.org/CONTENT/content-files/145463-x2-1.1.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel, gtksourceview2-devel, vte-devel

%description
X2 is an simple text/programming editor developed in house by Rock Computing
from a dissatisfaction with existing text editors. Features:
*) Small
*) Very light memory usage
*) Syntax highlighting
*) Embedded terminal
*) Find/replace/jump to line
*) Customizable file templates

%prep
%setup -q
sed -i 's|pixmaps/x2|pixmaps|' src/Makefile.in src/main.c

%build
%configure
make

%install
%{__rm} -rf %{buildroot}
%make_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/%{name}.*
%{_datadir}/pixmaps/%{name}.*

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuild for Fedora
