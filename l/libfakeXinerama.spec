%undefine _debugsource_packages

Name:           libfakeXinerama
Version:        0.1.0
Release:        11.1
URL:            https://www.xpra.org/trac/wiki/FakeXinerama
Summary:        Fake Xinerama library for exposing virtual screens
License:        MIT
Group:          System Environment/Libraries
Source:         http://xpra.org/src/%{name}-%{version}.tar.bz2
BuildRequires:  libXinerama-devel, libX11-devel
Requires:       filesystem-local

%description
This package provides a fake Xinerama library which can be used
to return pre-defined screen layout information to X11 client applications
which use the Xinerama extension.

%prep
%setup -q

%build
gcc -O2 -Wall fakeXinerama.c -fPIC -o libXinerama.so.1.0.0 -shared

%install
install -Dm755 libXinerama.so.1.0.0 %{buildroot}/usr/local/%{_lib}/libXinerama.so.1.0.0
ln -sf libXinerama.so.1.0.0 %{buildroot}/usr/local/%{_lib}/libXinerama.so.1

%clean
rm -rf %{buildroot}

%files
%doc README.TXT
/usr/local/%{_lib}/libXinerama.so.1*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Mon Mar 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuilt for Fedora
* Sat Feb 01 2014 Antoine Martin <antoine@devloop.org.uk - 0.1.0-1.0
- First version
