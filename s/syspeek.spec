Name:           syspeek
Version:        0.3bzr
Release:        9.1
Summary:        A system monitor indicator
License:        GPL-3.0+
Group:          System/GUI/GNOME
URL:            https://launchpad.net/syspeek
Source0:        https://launchpad.net/~nilarimogard/+archive/webupd8/+files/syspeek_0.3+bzr26.orig.tar.xz
BuildRequires:  intltool
BuildRequires:  python3-distutils-extra
BuildRequires:  pkgconfig(python3)
Requires:       python-appindicator
Requires:       libappindicator-gtk3
#Requires:      python-gtk
BuildArch:      noarch

%description
SysPeek displays CPU usage, memory usage, swap usage,
disk usage and network traffic.

%prep
%setup -q -c

%build
python3\
       setup.py \
       build

%install
install -D -m 644 \
        data/icons/256x256/apps/%{name}.svg \
        %{buildroot}%{_datadir}/pixmaps/%{name}.svg

python3\
       setup.py \
       install \
       -O1 \
       --skip-build \
       --root=%{buildroot} \
       --prefix=%{_prefix}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/22x22/status
cp data/icons/22x22/status/*.svg \
   %{buildroot}%{_datadir}/icons/hicolor/22x22/status

# Let's use %%doc macro.
rm -rf %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}/etc/xdg/autostart/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -rf %{buildroot}/etc

sed -i 's|/usr/bin/python$|/usr/bin/python3|' %{buildroot}%{_bindir}/%{name}

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{python3_sitelib}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/icons/hicolor/22x22/status/%{name}*

%changelog
* Mon Jul 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3bzr
- Rebuild for Fedora
* Mon May 12 2014 dap.darkness@gmail.com
- Initial build.
- Added syspeek-file-not-found.patch &
  syspeek-kde.patch to fix tray menu entries.
