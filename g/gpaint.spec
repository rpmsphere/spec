%undefine _debugsource_packages

Name:           gpaint
Version:        0.3.3
Release:        9.4
Summary:        Simple Paint Application
Group:          Applications/Graphics
License:        GPL
URL:            http://www.gnu.org/software/gpaint/
Source0:        ftp://alpha.gnu.org/gnu/gpaint/%{name}-2-%{version}.tar.gz
Source1:        gpaint-2.desktop
Source2:        gpaint-2.png
BuildRequires:  gtk2-devel, libgnomeui-devel, zlib-devel, libxml2-devel, libglade2-devel
BuildRequires:  w3m, udisks2
#BuildRequires:  libgnomeprint22-devel

%description
This is gpaint (GNU Paint), a small-scale painting program for GNOME, 
the GNU Desktop.  Gpaint does not attempt to compete with GIMP.  Think of GIMP 
is like Photoshop as gpaint is like Windows Paint.

%prep
%setup -q -n %{name}-2-%{version}
sed -i "s#GTK_RESPONSE_DISCARD#GTK_RESPONSE_NO#" src/drawing.c

%build
export CFLAGS="-lm -fPIC"
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
cp -a %{SOURCE1} %{buildroot}%{_datadir}/applications
cp -a %{SOURCE2} %{buildroot}%{_datadir}/pixmaps
%find_lang %{name}-2

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-2.lang
%doc ABOUT-NLS AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_bindir}/gpaint-2
%{_datadir}/gpaint
%{_datadir}/applications/gpaint-2.desktop
%{_datadir}/pixmaps/gpaint-2.png

%changelog
* Mon Jul 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3
- Rebuilt for Fedora
* Fri Apr 6 2007 James Lawrence <jimlawrnc@gmail.com> 0.3.0-pre5-1fc6
- new Spec file Initial RPM release for fedora core 6 
