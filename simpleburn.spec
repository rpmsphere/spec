%global debug_package %{nil}

Summary:	A basic burning tool
Name:		simpleburn
Version:	1.7.3
Release:	16.1
Group:		Archiving/Cd burning
License:	CeCILL-2
URL:		http://simpleburn.tuxfamily.org/
Source0:	http://simpleburn.tuxfamily.org/IMG/gz/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	wodim genisoimage
Requires:	vorbis-tools
Requires:	mpg123
Requires:	normalize

%description
SimpleBurn is a basic burning application for CDs and DVDs.

%prep
%setup -q

%build
%cmake \
	-DDETECTION=UDEV \
	-DBURNING=CDRTOOLS
sed -i 's|-std=c99|-std=c99 -fPIC -lm|' `find . -name *.make`
make

%install
%make_install
rm -rf %{buildroot}/usr/doc/
%find_lang %{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m755 src/lib*.so %{buildroot}%{_libdir}/%{name}

%files -f %{name}.lang
%doc doc/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}*
%{_datadir}/pixmaps/*.png
%{_libdir}/%{name}/lib*.so

%changelog
* Sat Apr 18 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.3
- Rebuild for Fedora
* Sun May 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.6.4-1
+ Revision: 800832
- imported package simpleburn

