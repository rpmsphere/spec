%undefine _debugsource_packages
Name: trans-purge
Version: 0.1
Release: 1
Summary: Linux Desktop Purge Tools
Summary(zh_TW): Linux 桌面瘦身工具
License: GPL
Group: Applications/System
Source0: http://pcman.sayya.org/desktop-purge.c
Source1: http://pcman.sayya.org/mime-purge.c
Source2: http://pcman.sayya.org/gconf-purge.c
Vendor: Hong Jen Yee (PCMan)   <pcman.tw( at )gmail.com>
BuildRequires: glib2-devel, pkgconfig

%description
Tools for purging other unused locale data after localepurge,
including desktop-purge, mime-purge and gconf-purge.

%description -l zh_TW
在 localepurge 之外用來移除系統中其他無用的多國語言翻譯，
工具包括 desktop-purge、mime-purge 和 gconf-purge。

%prep
%setup -T -c

%build
gcc `pkg-config glib-2.0 --cflags --libs` -o desktop-purge %{SOURCE0}
gcc `pkg-config glib-2.0 --cflags --libs` -o mime-purge %{SOURCE1}
gcc `pkg-config glib-2.0 --cflags --libs` -o gconf-purge %{SOURCE2}

%install
%__rm -rf %{buildroot}
%__install -Ds -m 755 desktop-purge %{buildroot}%{_bindir}/desktop-purge
%__install -Ds -m 755 mime-purge %{buildroot}%{_bindir}/mime-purge
%__install -Ds -m 755 gconf-purge %{buildroot}%{_bindir}/gconf-purge

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
