Name:          pyformex
Version:       0.9.1
Release:       10.4
Summary:       3D Geometry Designer
Group:         System/Libraries/Python
URL:           https://www.nongnu.org/pyformex/
Source:        https://download.savannah.gnu.org/releases/pyformex/%{name}-%{version}.tar.gz
License:       GPL
BuildRequires: python2-devel, python2-numpy, mesa-libGLU-devel, atlas-devel
#Requires: PyQt4

%description
pyFormex is a program for generating, transforming and manipulating large
geometrical models of 3D structures by sequences of mathematical operations.

%prep
%setup -q
sed -i 's|),|,|' pyformex/doc/html/_static/scripts/Helix.py

%build
python2 setup.py build

%install
rm -rf "$RPM_BUILD_ROOT"
python2 setup.py install \
   --root="$RPM_BUILD_ROOT" \
   --install-headers=%{_includedir}/python2.7 \
   --install-lib=%{python2_sitearch}

echo 'Categories=Development;' >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{python2_sitearch}/*

%changelog
* Mon Feb 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.1
- Rebuilt for Fedora
