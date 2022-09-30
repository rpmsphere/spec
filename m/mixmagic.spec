Summary: A hard drive sound mixer for Gnome
Name: mixmagic
Version: 0.1.7
Release: 2.1
License: GPL
Group: Applications/Multimedia
URL: http://mixmagic.sourceforge.net/
Source: http://download.sourceforge.net/zipcracker/%{name}-%{version}.tar.gz
BuildRequires: gcc automake
BuildRequires: gnome-libs-devel
BuildRequires: libxml-devel
BuildRequires: esound-devel

%description
MixMagic is a hard drive sound mixing program for Gnome, it can handle large
(larger then system memory) samples. MixMagic is able to mix as many waves
as your CPU can handle.

%prep
%setup -q
sed -i 's|gnome/apps/Multimedia|applications|' Makefile*

%build
CFLAGS="$RPM_OPT_FLAGS -Wno-format-security" ./configure $ARCH_FLAGS --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --target=%{_arch}-pc-linux-gnu
make

%install
make prefix=$RPM_BUILD_ROOT%{_prefix} install
%ifarch x86_64 aarch64
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
%endif
sed -i 's|gnome-mixmagic.png|multimedia-volume-control|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
echo 'Categories=AudioVideo;Mixer;' >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Thu Apr 30 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.7
- Rebuilt for Fedora
* Sat Apr 29 2000 Jonas Borgström <jonas_b@bitsmart.com>
- first try at an official RPM
