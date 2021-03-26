%global debug_package %{nil}

Name: linapple
Summary: Apple2 emulator for Linux
Version: 2a
Release: 13.1
Group: Emulators
License: GPL
URL: http://linapple.sourceforge.net/
Source0: http://sourceforge.net/projects/linapple/files/%{name}/%{name}-2a/%{name}-src_%{version}.tar.bz2
BuildRequires: gcc-c++, SDL-devel, libcurl-devel, libzip-devel

%description
Linapple is an emulator of Apple2 (Apple][, Apple 2, Apple2e) series computers
for Linux or other systems with SDL support, which works out of the box.
It derives from AppleWin, and almost as powerful as AppleWin is.

%prep
%setup -q -n %{name}-src_%{version}
sed -i '1i #include <unistd.h>' src/Timer.cpp src/Frame.cpp src/SerialComms.cpp

%build
cd src
make %{?_smp_mflags}

%install
cd src
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/images $RPM_BUILD_ROOT%{_libdir}/%{name}/ftp/cache
chmod -R 777 $RPM_BUILD_ROOT%{_libdir}/%{name}
install -m755 %{name} $RPM_BUILD_ROOT%{_libdir}/%{name}
install -m644 ../*.bmp ../Master.dsk $RPM_BUILD_ROOT%{_libdir}/%{name}
install -m644 ../linapple.installed.conf $RPM_BUILD_ROOT%{_libdir}/%{name}/linapple.conf
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_libdir}/%{name}
./%{name}
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc CHANGELOG LICENSE README
%{_bindir}/%{name}
%{_libdir}/%{name}

%clean
%__rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2a
- Rebuild for Fedora
