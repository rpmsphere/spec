%define kver %(uname -r)
# Conditional build:
%bcond_without	dist_kernel	# without kernel from distribution
%bcond_without	kernel		# don't build kernel modules
%bcond_without	userspace	# don't build userspace utilities
%bcond_with	verbose		# verbose build (V=1)
#
%define		rel	16
Summary:	Bluetooth-alsa Project
Summary(pl.UTF-8):	Projekt Bluetooth-alsa
Name:		btsco
Version:	0.5
Release:	%{rel}
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/bluetooth-alsa/%{name}-%{version}.tgz
# Source0-md5:	d9fdd63a9e22ba839a41c8a9b89c2dda
Patch0:		%{name}-readme-pl.diff
Patch1:		%{name}-kernel.patch
URL:		http://sourceforge.net/projects/bluetooth-alsa/
%if %{with kernel}
%{?with_dist_kernel:BuildRequires:	kernel-devel}
%endif
%if %{with userspace}
#BuildRequires:	alsa-driver-devel >= 1.0.9-1
BuildRequires:	alsa-lib-devel >= 1.0.9-1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 2.21-1
BuildRequires:	libao-devel >= 0.8.6-1
BuildRequires:	libtool
#BuildRequires:	rpmbuild(macros) >= 1.379
%endif

%description
This project provides a way to use a bluetooth headset with Linux. We
do this currently by making an alsa kernel driver which uses bluez to
reach the headset. It works well enough now to get voice-quality audio
to and from most headsets.

%description -l pl.UTF-8
Dzięki temu oprogramowaniu można używać zestawów słuchawkowych
Bluetooth Headset z Linuksem. Osiągnięto to dzięki zbudowaniu alsowego
modułu do jądra, który to używa systemu bluez do komunikacji z takim
zestawem. Współpracuje z większością zestawów, ograniczeniem w
komunikacji jest często urządzenie USB, które to może mieć
nieobsługiwane częściowo protokoły, wskazówka: hciconfig hciXXX
revision. W skrajnym wypadku można próbować użyć innego urządzenia
USB.

%package kmod
Summary:	Linux ALSA kernel driver for Bluetooth Headset
Summary(pl.UTF-8):	Sterownik ALSA do jądra Linuksa dla Bluetooth Headset
##Release:	%(echo %{kver} | tr - _).%{rel}
Group:		Base/Kernel
#%{?with_dist_kernel:%requires_releq_kernel}
Requires(post,postun):	/sbin/depmod
#Requires:	kernel%{_alt_kernel}-sound-alsa
Requires:	alsa-lib

%description kmod
Linux ALSA kernel driver for Bluetooth Headset named snd_bt_sco.

%description kmod -l pl.UTF-8
Sterownik ALSA do jądra Linuksa dla Bluetooth Headset o nazwie
snd_bt_sco.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%if %{with userspace}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
%endif

%if %{with kernel}
#%build_kernel_modules -m snd-bt-sco -C kernel
make -C kernel
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d $RPM_BUILD_ROOT%{_bindir}

for file in avdtp/avtest sbc/rcplay sbc/sbcenc sbc/sbcinfo a2play btsco2 btsco ; do
	install $file $RPM_BUILD_ROOT%{_bindir}
done
%endif

%if %{with kernel}
#%install_kernel_modules -m kernel/snd-bt-sco -d misc
install -Dm 744 kernel/snd-bt-sco.ko %{buildroot}/lib/modules/%{kver}/misc/snd-bt-sco.ko
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc README README.PL.txt
%attr(755,root,root) %{_bindir}/*
%endif

%if %{with kernel}
%files kmod
%defattr(644,root,root,755)
/lib/modules/%{kver}/misc/snd-bt-sco.ko
%endif


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri May 30 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.5-16.ossii
- Build for M6(CentOS5)

* Thu Mar 27 2008 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: btsco.spec,v $
Revision 1.37  2008-03-27 22:27:13  glen
- rel 16 (2.6.22.19-5)

Revision 1.36  2008-03-10 12:21:12  arekm
- release 15

Revision 1.35  2008-02-11 11:31:49  arekm
- rel 14

Revision 1.34  2008-01-22 22:53:46  glen
- rel 13 (2.6.16.59-2)

Revision 1.33  2007-12-17 14:17:28  arekm
- rel 12

Revision 1.32  2007-12-15 11:57:04  arekm
- rel 11

Revision 1.31  2007-11-29 08:01:25  arekm
- rel 10

Revision 1.30  2007-11-25 10:32:41  arekm
- rel 9

Revision 1.29  2007-10-24 13:50:41  arekm
- rel 8

Revision 1.28  2007/10/12 12:48:36  arekm
- rel 7

Revision 1.27  2007/08/05 05:09:00  wolvverine
- rel.6

Revision 1.26  2007/07/27 22:21:55  wolvverine
- rel.5

Revision 1.25  2007/07/17 23:27:52  shadzik
- don't call make with strange -Wall function
  (it doesn't pass -Wall functionality to gcc, instead it breaks userspace build)

Revision 1.24  2007/07/12 20:16:29  blekot
- now builds with kernel 2.6.21

Revision 1.23  2007/06/11 17:14:16  blekot
- added kernel patch (fixes snd_bt_sco: Unknown symbol try_to_freeze)
- STBR

Revision 1.22  2007/06/08 21:40:44  arekm
- rel 3

Revision 1.21  2007/04/20 10:23:48  pluto
- bump release and rebuild with 2.6.20.7.

Revision 1.20  2007/04/12 15:16:25  shadzik
- proper kernel-module-build version

Revision 1.19  2007/04/02 03:32:53  shadzik
- use new kernel macros
- remove smp stuff

Revision 1.18  2007/03/14 00:13:57  glen
- up bcond

Revision 1.17  2007/02/12 21:23:49  glen
- tabs in preamble

Revision 1.16  2007/02/12 00:48:40  baggins
- converted to UTF-8

Revision 1.15  2006/12/29 09:26:04  lmasko
- %{_alt_kernel} macro works now

Revision 1.14  2006/12/03 15:27:36  shadzik
- use new %build_kernel_modules macros

Revision 1.13  2006/12/03 15:18:03  shadzik
- 0.5

Revision 1.12  2006/10/29 03:44:21  shadzik
- 0.42

Revision 1.11  2006/09/06 13:48:33  sparky
- mass atack: -j1 for make scripts

Revision 1.10  2006/08/27 10:39:16  arekm
- rel 3; rebuild

Revision 1.9  2006/06/27 00:02:25  wolvverine
- add BR

Revision 1.8  2006/04/12 12:15:40  glen
- add kernel epoch, adapterized

Revision 1.7  2006/04/09 09:44:45  aflinta
- fixed smp scripts, release 2

Revision 1.6  2006/04/04 05:24:32  wolvverine
- up to 0.41

Revision 1.5  2006/04/04 00:52:17  wolvverine
- correct log

Revision 1.4  2006/04/04 00:47:52  wolvverine
- patch from Lukasz Masko ed <at> yen <dot> ipipan <dot> waw <dot> pl

Revision 1.3  2005/12/03 10:39:19  qboosh
- revised docs and userspace build
- I don't see any reason for ExclusiveArch

Revision 1.2  2005/12/03 10:04:45  qboosh
- userspace bcond, cosmetics

Revision 1.1  2005/11/28 19:26:46  abram
- initial
- works on i686, but i can not test it on other platforms
