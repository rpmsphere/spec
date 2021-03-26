Name:         wmgtemp
Release:      3.1
License:      Artistic License
URL:          http://www.fluxcode.net/
Group:        System/GUI/Other
Version:      1.1
Summary:      Display the CPU and SYS temperatures
Source:       http://www.fluxcode.net/wmgtemp-%{version}.tar.gz
BuildRequires: libX11-devel, libXpm-devel, libXext-devel
BuildRequires: lm_sensors-devel

%description
wmgtemp is a dock-app for Window Maker that graphically displays the
CPU and System temperatures using the lm_sensors package. It
displays the CPU and System temperature values, a scaling graph of
temperature history, high-temperature warning lights and
temperatures in degrees Celsius, Fahrenheit or Kelvin.

%prep
%setup
sed -i -e 's/sensors\.conf/sensors3.conf/' src/wmgtemp.c
sed -i 's|INLINE ||' src/wmgeneral/list.?
#sed -i 's|inline void cycle_temptype|void cycle_temptype|' src/wmgtemp.c
#sed -i 's|inline void draw_type|void draw_type|' src/wmgtemp.c
#sed -i 's|inline void blank_type|void blank_type|' src/wmgtemp.c
sed -i 's|inline void|void|' src/wmgtemp.c
sed -i 's|-lX11|-lX11 -Wl,--allow-multiple-definition|' src/Makefile

%build
find -type f | xargs chmod 644
make LIB=%{_lib} CCFLAGS+="-Wall %{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 src/wmgtemp $RPM_BUILD_ROOT%{_bindir}
install -m 644 wmgtemp.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc INSTALL README TODO Artistic BUGS CREDITS examples/wmgtemprc
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sun Sep 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
* Tue Jun 22 2010 Ludwig Nussel <lnussel@suse.de>
- new version 1.1 includes previous patch
* Mon Jun 21 2010 Ludwig Nussel <lnussel@suse.de>
- new version 1.0 works with lm_sensors3
* Tue Jul  1 2008 Ludwig Nussel <lnussel@suse.de>
- initial package version 0.8
