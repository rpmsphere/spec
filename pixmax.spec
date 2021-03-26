%global debug_package %{nil}

Summary: A simple 3d-plot utility
Name: pixmax
Version: 2.2
Release: 7.1
License: GPL
Group: Applications/Multimedia
URL: http://vento.pi.tu-berlin.de/pixmax/main.html
Source: http://vento.pi.tu-berlin.de/%{name}/%{name}-%{version}.src.tar.gz

%description
The pixmax utility allows the plotting of 3d-data sets.
Pixmax is a batch oriented program. It generates raster files
in PPM-format as output.

%prep
%setup -q
sed -i 's/getline/mygetline/' src/*

%build
make -C src

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -m 755 src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 644 fonts/* $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts
install -m 644 man/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%doc README COPYING CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/%{name}

%changelog
* Tue Dec 23 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuild for Fedora
