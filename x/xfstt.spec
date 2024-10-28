Summary:   X Font Server for *.ttf fonts
Name:      xfstt
Version:   1.11
Release:   1
Source:    https://fossies.org/linux/misc/xfstt-%{version}.tar.xz
Source1:   xfstt.init
License:   LGPL
Group:     X11/Utilities

%description
xfstt means "X11 Font Server for TrueType fonts".
TT fonts are generally regarded to be the best scalable fonts
for displays. Applications that need scalable fonts for display
on low resolution devices like screens benefit most.

%prep
%setup -q

%build
%configure
make MISCOPT="$RPM_OPT_FLAGS"

%install
%make_install
install -Dm755 %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfstt
mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/fonts/ttfonts

%pre
# adds "inet/127.0.0.1:7100" to the list of searchable fonts
if [ -r /etc/X11/XF86Config ]; then
   if grep "FontPath.*7100" /etc/X11/XF86Config > /dev/null
   then
      /bin/true
   else
      LINE=`grep -n "FontPath" /etc/X11/XF86Config | cut -d: -f1 | tail -1`
      TOTAL=`wc -l < /etc/X11/XF86Config`
      head -$LINE /etc/X11/XF86Config > /tmp/XF86Config.$$ \
      && echo "FontPath   \"inet/127.0.0.1:7100\"" >> /tmp/XF86Config.$$ \
      && tail -`expr $TOTAL - $LINE` /etc/X11/XF86Config >> /tmp/XF86Config.$$ \
      && cat /tmp/XF86Config.$$ > /etc/X11/XF86Config \
      && rm /tmp/XF86Config.$$
   fi
else
   echo "To use xfstt font automatically add :"
   echo "inet/127.0.0.1:7100"
   echo "To your Xservers fontpath"
   echo "For AcceleratedX see the [FONTPATH] section"
fi

%post
/usr/sbin/chkconfig --add xfstt

%preun
if [ "$1" = 0 ] ; then
    /usr/sbin/chkconfig --del xfstt
fi

%postun
if [ -r /etc/X11/XF86Config ]; then
    egrep -v "FontPath.*7100" /etc/X11/XF86Config > /etc/X11/XF86Config.$$ ;
    mv /etc/X11/XF86Config.$$ /etc/X11/XF86Config
fi

%files
%doc NEWS COPYING* README THANKS TODO
%config /etc/rc.d/init.d/xfstt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%dir %{_datadir}/X11/fonts/ttfonts

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11
- Rebuilt for Fedora
* Sun Jul 19 1998 Jeff Johnson <jbj@redhat.com>
- repackage for powertools.
* Tue Jun 02 1998 Arne Coucheron <arneco@online.no>
- updated to 0.9.9-1
- changed the init script to behave better
- changed the ttfonts dir from /usr/ttfonts to /usr/X11R6/lib/X11/fonts/ttfonts
- using %%{name} and %%{version} macros
- using %%defattr macro in filelist
- added use of $RPM_OPT_FLAGS
- added striping of the binary
* Tue May 12 1998 Kjetil Wiekhorst Jorgensen <jorgens@pvv.org>
- Added more to the %%pre, %%post, %%preun and %%postun tag to the specfile
* Tue May 5 1998  Ian Macdonald <ianmacd@xs4all.nl>
- Added post-install and post-uninstall scripts
* Thu Apr 30 1998  Ian Macdonald <ianmacd@xs4all.nl>
- Re-added start-up script for xfstt
