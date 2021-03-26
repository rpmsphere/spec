Name:           enlightenment
Version:        0.16.999.063
Release:        9%{?dist}
Summary:        Highly optimized and extensible desktop shell

Group:          User Interface/Desktops
License:        MIT
URL:            http://enlightenment.org/p.php?p=about/e17&l=en
Source0:        http://download.enlightenment.org/snapshots/2009-06-14/%{name}-%{version}.tar.bz2
Source1:	enlightenment-sysactions.conf
Source2:	fireball.edj
Source3:	oxim.imc
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libX11-devel libXext-devel pkgconfig gettext
BuildRequires:  eet-devel embryo-devel evas-devel ecore-devel edje-devel
BuildRequires:  efreet-devel e_dbus-devel pam-devel libeina-devel
#BuildRequires:  exchange-devel alsa-lib-devel
BuildRequires:  alsa-lib-devel
Requires:		pm-utils

%description
Enlightenment 0.17 is desktop shell based on Enlightenment Foundation
Libraries. It's highly optimized and provides extensive theming capabilities.
A Desktop shell means it's a window manager plus a file manager, plus 
configuration utilitys all in one. It works reasonably fast even on old and low
range computers, providing eye-candy environment.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       eet-devel evas-devel ecore-devel edje-devel e_dbus-devel
Requires:       pkgconfig efreet-devel libeina-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
# strip out bundled vera font, it doesn't support national glyphs
#rm -r data/fonts
sed -i \
  -e '\|CONFIG_FILES="\$CONFIG_FILES data/fonts/Makefile"|d' \
  -e 's|data/fonts/Makefile||' \
  configure #; chmod +x configure
#sed -i -e 's|fonts||' data/Makefile.in
# remove font aliases to make edje fall back to default font (dejavu)
#sed -i -e '\|\.ttf|d' data/{init,themes}/default.edc
# backport enlightenment.pc.in fix from trunk
#sed -i -e 's|Libs:\ .*$|Libs: -L${libdir}|' enlightenment.pc.in


%build
export LDFLAGS="-lecore_x -lm -ldbus-1 -leina"
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
# config.h is used only while building E itself
sed -i -e '\|#include\ "config.h"|d' $RPM_BUILD_ROOT%{_includedir}/%{name}/e.h
find $RPM_BUILD_ROOT -name '*.la' -delete
# remove improperly placed docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/AUTHORS
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/COPYING
# remove enlightenment_sys which is broken anyway
#rm -rf $RPM_BUILD_ROOT%{_bindir}/%{name}_sys
#rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sysactions.conf
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sysactions.conf
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/data/backgrounds/fireball.edj
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}/data/input_methods/oxim.imc
%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING-PLAIN README
%{_bindir}/%{name}
%{_bindir}/%{name}_*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_sysconfdir}/%{name}


%files devel
%defattr(-,root,root,-)
# originally improperly placed docs
%doc doc/*.txt doc/*.html doc/*.png
#%{_bindir}/%{name}-config
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/everything.pc


%changelog
* Fri May 14 2010 Victor Horng <victor@ossii.com.tw> 0.16.999.063-6
- Add fireball.edj
- Add oxim.imc
- Change lang-zh_TW.png
