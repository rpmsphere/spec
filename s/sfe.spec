%undefine _debugsource_packages

Name:           sfe
Version:        0.2a
Release:        3.1
Summary:        Small Fractal Explorer
Group:		Games and Entertainment
License:       GPL 
URL:	https://bruxy.regnet.cz/web/programming/EN/small-fractal-explorer	
Source0:	%{name}-%{version}.tar.gz
BuildRequires: SDL-devel 
Requires:       SDL

%description
Small Fractal Exporer (sfe) is a simple Manderbrot set and Julia set generator.
You can just click on left side of the screen (in Mandelbrot set complex plane)
to choose start seed. The start seed point is value from the Mandelbrot set
which is used for Julia set computation. When the point lies in the Mandelbrot
set, the Julia set is connected. Otherwise, the Julia set is a Cantor dust of
unconnected points. The result is a wonderful picture!

%prep
%setup -q
sed -i 's|gcc|gcc -Wl,--allow-multiple-definition|' Makefile

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
cp -p sfe %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}/
cp -p README %{buildroot}%{_defaultdocdir}/%{name}-%{version}/

#make install INSTALL_DIR=$RPM_BUILD_ROOT INSTALL_DOC=$RPM_BUILD_ROOT

%files
/usr/bin/sfe
%doc /usr/share/doc/sfe-%{version}/README

%changelog
* Mon Mar 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2a
- Rebuilt for Fedora
* Wed Aug  8 2012 Martin Bruchanov <bruxy@regnet.cz> - 0.2a
- RPM package
