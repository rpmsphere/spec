Name: flash-plugin
Summary: Adobe Flash Player
Version: 10.0.45.2
Release: 3%{?dist}.bin
License: Commercial
Group: Applications/Internet
URL: http://labs.adobe.com/technologies/flashplayer10/
Source0: http://fpdownload.macromedia.com/get/flashplayer/current/install_flash_player_10_linux.tar.gz
# http://www.adobe.com/products/eulas/
Source1: http://www.adobe.com/products/eulas/pdfs/Reader_Player_WWEULA-Combined-20060724_1430.pdf
Source2: http://download.macromedia.com/pub/labs/flashplayer10/libflashplayer-%{version}.linux-x86_64.so.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
#ExclusiveArch: i686 x86_64
BuildRequires: chrpath

%description
Adobe Flash Player

By downloading and installing this package you agree to the included
End-User License Agreement:

http://www.adobe.com/products/eulas/players/flash/

%prep
%ifarch x86_64
%setup -q -c -T -a 2
%else
%setup -q -c
%endif
%{__install} -pm644 %{SOURCE1} ./

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 libflashplayer.so %{buildroot}%{_libdir}/flash-plugin/libflashplayer.so
chrpath -d %{buildroot}%{_libdir}/flash-plugin/libflashplayer.so
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins/
ln -sf ../../flash-plugin/libflashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Reader_Player_WWEULA*.pdf
%{_libdir}/flash-plugin/libflashplayer.so
%{_libdir}/mozilla/plugins/libflashplayer.so

%changelog
* Wed Aug 25 2010 Wei-Lun Chao <bluebat@member.fsf.org> - 10.0.45.2-3
- Rebuild for OSSII

* Sun Feb 14 2010 Paulo Roma <roma@lcg.ufrj.br> - 10.0.45.2-2
- Updated to 10.0.45.2

* Thu Dec 10 2009 Paulo Roma <roma@lcg.ufrj.br> - 10.0.42.34-2
- Updated to 10.0.42.34

* Tue Nov 17 2009 Paulo Roma <roma@lcg.ufrj.br> - 10.0.32.18-2
- Installing in /usr/lib64/flash-plugin/

* Fri Jul 31 2009 Paulo Roma <roma@lcg.ufrj.br> - 10.0.32.18-1
- Updated to 10.0.32.18

* Mon Jan 26 2009 Paulo Roma <roma@lcg.ufrj.br> - 10.0.22.87-1
- Updated to 10.0.22.87

* Mon Jan 26 2009 Paulo Roma <roma@lcg.ufrj.br> - 10.0.21.1-1
- Updated to 10.0.21.1

* Mon Nov 17 2008 Dominik Mierzejewski <rpm@greysector.net> - 10.0.20.7-1
- Add 10.0.20.7 beta for x86_64

* Thu Oct 16 2008 Dominik Mierzejewski <rpm@greysector.net> - 10.0.12.36-1
- Updated to 10 final

* Thu Aug 28 2008 Dominik Mierzejewski <rpm@greysector.net> - 10.0.0.569-1
- Updated to 10 beta build 569
- Use EULA from Adobe's website
- Fix summary and description

* Thu May 15 2008 Dominik Mierzejewski <rpm@greysector.net> - 10.0.0.218-1
- Updated to 10 beta build 218

* Thu Dec 20 2007 Dominik Mierzejewski <rpm@greysector.net> - 9.0.115.0-1
- Updated to 9.0.115.0 (security update)

* Tue Oct 23 2007 Dominik Mierzejewski <rpm@greysector.net> - 9.0.48.0-1
- Updated to 9.0.48.0

* Fri Jun 15 2007 Dominik Mierzejewski <rpm@greysector.net> - 9.0.31.0-2
- Updated to update3 beta.

* Tue Feb 20 2007 Dominik Mierzejewski <rpm@greysector.net> - 9.0.31.0-1
- Updated to release.

* Mon Nov 27 2006 Dominik Mierzejewski <rpm@greysector.net> - 9.0.21.78-1
- Updated to beta2.

* Fri Oct 20 2006 Dominik Mierzejewski <rpm@greysector.net> - 9.0.21.55-1
- Updated to latest beta.
- Renamed to flash-plugin.

* Wed Mar 15 2006 Dag Wieers <dag@wieers.com> - 7.0.63-1 - 3737+/dag
- Updated to release 7.0.63.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 7.0.61-1
- Updated to release 7.0.61.

* Sun Jun 27 2004 Dag Wieers <dag@wieers.com> - 7.0.25-1
- Initial package. (using DAR)
