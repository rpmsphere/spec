Name: oto
Summary: Open Type Organizer
Version: 0.5
Release: 2.1
License: GPL
Group: Development/Tools
URL: http://sourceforge.net/projects/oto
Source: http://sourceforge.net/projects/oto/files/%{name}/%{version}/%{name}-%{version}.tar.gz

%description
Open Type Organizer provides programs to list, modify OpenType
font files, specifically, their 'name' and 'cmap' tables.
It can be used to translate 'name' and 'cmap' of OpenType font
from locale encodings to Unicode encoding so the font file can be
used in environment which does not understand locale encodings.
The translated tables are added to the font while keeping the
original tables intact.

%prep
%setup -q

%build
%configure
make

%install
rm -fr ${buildroot}
%makeinstall

%clean
rm -fr ${buildroot}

%files
%{_bindir}/*
%{_datadir}/*
%doc AUTHORS COPYING INSTALL NEWS README ChangeLog

%changelog
* Mon May 25 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuild for Fedora
* Fri Sep 23 2005 Yao Zhang <yaoz@users.sourceforge.org>
- Initial package
