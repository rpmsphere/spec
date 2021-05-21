%define upstream_name GNS3

Name:           gns3
Version:        0.8.7
Release:        4.4
Summary:        Graphical network simulator
License:        GPLv2+
Group:          Emulators
URL:            http://www.gns3.net/
Source0:        http://downloads.sourceforge.net/gns-3/%{upstream_name}-%{version}-src.tar.gz
Source1:        http://downloads.sourceforge.net/gns-3/%{upstream_name}-0.5-tutorial.pdf
Source10:       %{name}.png
BuildRequires:  python-qt4
BuildRequires:  python2-devel
BuildRequires:  qt4-devel
BuildRequires:  sip-devel
BuildRequires:  dos2unix
BuildArch:      noarch
Requires:       PyQt4
Requires:       sip
Requires:       dynamips
Requires:       hicolor-icon-theme
Requires:       xterm

%description
GNS3 is an excellent complementary tool to real labs for network engineers,
administrators and people wanting to study for certifications such as Cisco
CCNA, CCNP, CCIP and CCIE as well as Juniper JNCIA, JNCIS and JNCIE.

It can also be used to experiment features of Cisco IOS, Juniper JunOS or to
check configurations that need to be deployed later on real routers.

Thanks to VirtualBox integration, now even system engineers and administrators
can take advantage of GNS3 to study Redhat (RHCE, RHCT), Microsoft (MSCE,
MSCA), Novell (CLP) and many other vendor certifications.

%prep
%setup -q -n %{name}-legacy-%{upstream_name}-%{version}
sed -i 's|usr/local|usr|' setup.py

%build
cp %{_sourcedir}/%{upstream_name}-0.5-tutorial.pdf .

%install
python2 setup.py install --root=%{buildroot} --prefix=%{_prefix}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

mkdir -p %{buildroot}%{_datadir}/%{name}/examples
mv %{buildroot}%{_datadir}/examples/%{name}/*.txt %{buildroot}%{_datadir}/%{name}/examples
rm -rf %{buildroot}%{_datadir}/examples

rm -rf %{buildroot}%{_datadir}/doc/%{name}
#prepare docs
chmod -x AUTHORS README CHANGELOG COPYING TODO
dos2unix README

#shortcut
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{upstream_name}
Comment=Graphical Network Simulator
Exec=%{name} 
Terminal=false
Type=Application
StartupNotify=true
Icon=%{name}
Categories=Development;
MimeType=application/x-gns3;
EOF

#associate *.net files with gns3
mkdir -p %{buildroot}%{_datadir}/mime/packages
cat > %{buildroot}%{_datadir}/mime/packages/%{name}.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/x-gns3">
    <comment>%{upstream_name} Project</comment>
    <glob pattern="*.net"/>
    <sub-class-of type="application/xml"/>
  </mime-type>
</mime-info>
EOF

#install icons
install -m 644 -p -D %{_sourcedir}/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -m 644 -p -D %{_sourcedir}/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/mimetypes/application-x-%{name}.png

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc AUTHORS README CHANGELOG COPYING TODO %{upstream_name}-0.5-tutorial.pdf
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/64x64/mimetypes/application-x-%{name}.png
%{_mandir}/man?/*
%{_datadir}/%{name}
#{_datadir}/%{name}/baseconfig.txt
#{_datadir}/%{name}/baseconfig_sw.txt
#{_usr}/lib/%{name}
%{python_sitelib}/%{upstream_name}/*
%{python_sitelib}/%{upstream_name}-%{version}-py*.egg-info

%changelog
* Fri Nov 28 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.7
- Rebuilt for Fedora
* Sat Jan 12 2013 umeabot <umeabot> 0.8.3.1-2.mga3
+ Revision: 352319
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sat Dec 01 2012 kamil <kamil> 0.8.3.1-1.mga3.nonfree
+ Revision: 324552
- remove P2 - merged upstream
* Sat Aug 18 2012 kamil <kamil> 0.8.3-1.mga3.nonfree
+ Revision: 282062
- new version 0.8.3
- rediff P1, P2
- new install directories of *.py scripts
- add P2: -mga-fix-VBOXWRAPPER_DEFAULT_PATH
* Sat Apr 14 2012 kamil <kamil> 0.8.2-4.mga2.nonfree
+ Revision: 230816
- stop suggesting xterm (replaced with universal xvt)
* Sat Apr 14 2012 kamil <kamil> 0.8.2-3.mga2.nonfree
+ Revision: 230815
- add P1 mga-use-xvt-as-the-default-terminal.patch
* Sat Apr 14 2012 kamil <kamil> 0.8.2-2.mga2.nonfree
+ Revision: 230737
- suggest python-virtualbox
* Wed Mar 28 2012 kamil <kamil> 0.8.2-1.mga2.nonfree
+ Revision: 227265
- new (stable) version GNS3 0.8.2
- stop displaying URPMI warning (no need for it anymore)
* Sun Feb 05 2012 kamil <kamil> 0.8.2-0.BETA2.2.mga2.nonfree
+ Revision: 205059
- remove deprecated macro %%{py_requires}
- rename patch P0 to match policies
- new version 0.8.2-BETA2
- rediff P0 and use now environtment TMP/TEMP as a working dir
- new version 0.8.2-BETA2
- rediff patch and use now default working, project and images directories
* Fri Jan 13 2012 kamil <kamil> 0.8.2-0.BETA.1.mga2.nonfree
+ Revision: 195605
- include README.urpmi with warning on missing UDP feature in QEMU and project directories
* Fri Jan 13 2012 kamil <kamil> 0.8.2-0.BETA.0.mga2.nonfree
+ Revision: 195565
- new version 0.8.2-BETA
- new suggestion virtualbox >= 4.1
- removed coreutils from suggestions
- patch src-paths fixing paths rediffed
- new kind of installation, without "python2 setup.py build" in %%build
- extra files (qemuwrapper, vboxwrapper, vboxcontroller_4_1,  baseconfig.txt) are installed now into /usr/share/gns3/ and this is done now by the new installation and patch src-paths)
- remove X-MandrivaLinux-MoreApplications-Emulators from the .desktop file
- clean .spec
* Sat Nov 12 2011 kamil <kamil> 0.7.4-2.mga2
+ Revision: 166950
- build requirements updated
- requirements and suggestions updated
- included documentation in pdf
- patch default paths for qemuwrapper, dynamips, projects and images
- icon included
- link *.net files to gns3
- removed old file 0.7 from binrepo
- description updated
- package cleaning
* Mon Jun 27 2011 buchan <buchan> 0.7.4-1.mga2
+ Revision: 114711
- New version 0.7.4
* Sat May 07 2011 dmorgan <dmorgan> 0.7-1.mga1
+ Revision: 95895
- imported package gns3
