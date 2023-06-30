%define __python /usr/bin/python2
Name: moeclock
Summary: Moe Desktop Clock
Version: 1.2.0.2
Source0: %{name}.tar.gz
Source1: moeskin_suse.tar.gz
Patch0:  default-setting.patch
Patch1:  desktop-entry.patch
Release: 33.1
License: GNU General Public License v3 and CC-BY and Restrictive
Group: Amusements/Toys/Clocks
URL: https://code.google.com/p/moeclock/
BuildArch: noarch
BuildRequires: python2-devel
Requires: pygtk2, gnome-python2

%description
moeclock is Moe Desktop Clock.

%description -l ja
萌え時計は1分ごとに萌え絵が切り替わる時計です。
萌え絵は含んでおりませんので、ご自身でお好きな萌え絵を集めて、
ご自身のお気に入りの萌え時計を作ることができます。
もし1440枚集めれば、1日24時間すべて違う萌え絵を楽しむこともできます。

%prep
%setup -q -c
%patch0
%patch1

# デバッグメッセージを出力しないようにする
sed -i 's|^\(.*\)\(moeclock\.py\)\(.*\)$|\1\2\3 > /dev/null|' moeclock

%build
%{__python} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__python} setup.py install --prefix=%{_prefix} --root $RPM_BUILD_ROOT --install-lib=%{python_sitelib}
tar xf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/%{name}/

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}.py
sed -i 's|^python |python2 |' %{buildroot}%{_bindir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc README.txt
%dir %{_datadir}/%{name}
# GPL
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*.glade
%{_datadir}/%{name}/*.py*
%{_datadir}/%{name}/*.txt
%{python_sitelib}/%{name}-*.egg-info
# CC-BY
%{_datadir}/%{name}/moeclock.png
%{_datadir}/%{name}/default
%{_datadir}/%{name}/mikunchu
%{_datadir}/%{name}/moeskin*
# 時報ファイルの改変および単体での再配布は許可されていません
# 萌え時計のアーカイブとしてアプリケーションに含まれた形での再配布であればOKです。
%{_datadir}/%{name}/sound*

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0.2
- Rebuilt for Fedora
* Wed Apr 25 2012 kobayashi
- Rebuild for SUSE
- Skin update
* Fri Feb 11 2011 Sawa <sawa@ikoinoba.net> - 1.2.0.0-1
- Initial package.
