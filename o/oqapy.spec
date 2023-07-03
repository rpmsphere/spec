Name: 	 	oqapy
Summary: 	An application intended to sort files of the image type in graphic mode
Version: 	1.9.1
Release: 	3.1
Source:		https://www.oqapy.eu/releases/%{name}-%{version}.tar.gz
URL:		https://www.oqapy.eu/
License:	GPLv3
Group:		Applications/Multimedia
Requires:	PyQt4
Requires:	pyexiv2
Requires:	gphoto2
Requires:	python-pillow
#Requires:	jre
BuildArch:	noarch

%description
Various options make it possible to use it like simple viewer or to apply some
basic modifications to the image itself like to the properties of the file.
Features :
* Seek and sorting of images in the local folders by names, dates, sizes, tags, etc ;
* Management of the metadata, allowing to modify, in the header of the image, author, copyright, tags, etc ;
* Realignment and redimensioning ;
* Simple viewer mode and full screen mode ;
* Import from digital camera ;
* Export on various formats ;
* Diaporama ;
* Layout and printing ;
* Geolocalisation.

%prep
%setup -q
sed -i 's|^import Image|from PIL import Image|' warningDialog.py

%build

%install
mkdir -p %{buildroot}%{_bindir}
mv %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
mv %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/pixmaps
mv %{name}_ic_48.png %{buildroot}%{_datadir}/pixmaps/%{name}_ic_48.png
mkdir -p %{buildroot}%{_mandir}/man1
mv %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
mkdir -p %{buildroot}%{_datadir}/doc
mv doc %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_ic_48.png
%{_mandir}/man1/%{name}.1.*
%{_datadir}/%{name}

%changelog
* Sun Jan 19 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.1
- Rebuilt for Fedora
