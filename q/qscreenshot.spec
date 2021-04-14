Name:           qscreenshot
Version:        1.0
Release:        1
Summary:        Qt screenshot tool
License:        GPLv2
Group:          Graphics/Utilities
URL:            https://sourceforge.net/projects/qscreenshot
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}-%{version}-src.tar.gz
BuildRequires:  pkgconfig(QtCore)

%description
A fast and lightweight application used for capturing screenshots,
then editing and uploading them to various online image hosting services

qScreenshot is an intuitive tool that allows you to capture your desktop
or only parts of it, then edit the screenshots.

In addition, you can rely on this software to upload your screenshots
to specified hosting servers to share them with greater ease.
Here are some key features of \"qScreenshot\":
Capture the entire desktop, the specified area or the active window
Edit screenshots with the built simple graphic editor
Open an existing image from your local disk
Management via an icon in the system tray system

%prep
%setup -q -n %{name}

%build
%qmake_qt4
%make_build

%install
%makeinstall INSTALL_ROOT=%{buildroot}
mv %{buildroot}%{_bindir}/qScreenshot %{buildroot}%{_bindir}/%{name}

# Add translation lang tags
(cd %{buildroot} && find . -name '*.qm') | %__sed -e 's|^.||' | sed -e \
    's:\(.*/translations/qscreenshot_\)\([a-z_A-Z]\+\)\(.*qm$\):%lang(\2) \1\2\3:'\
        >> %{name}.lang

%files -f %{name}.lang
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/qscreenshot.desktop

%changelog
* Fri Jan 03 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Sun Sep 23 2018 umeabot <umeabot> 1.0-6.mga7
  (not released yet)
+ Revision: 1300677
- Mageia 7 Mass Rebuild
* Tue Feb 16 2016 umeabot <umeabot> 1.0-5.mga6
+ Revision: 962531
- Mageia 6 Mass Rebuild
* Tue Oct 20 2015 danf <danf> 1.0-4.mga6
+ Revision: 892910
- Use %%qmake_qt4 to configure so debuginfo gets built
* Wed Oct 15 2014 umeabot <umeabot> 1.0-3.mga5
+ Revision: 740751
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 1.0-2.mga5
+ Revision: 688516
- Mageia 5 Mass Rebuild
* Sat Aug 09 2014 dglent <dglent> 1.0-1.mga5
+ Revision: 661235
- imported package qscreenshot
