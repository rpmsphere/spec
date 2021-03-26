Name: xpybutil
Summary: An abstraction over the X Python Binding
Version: 0.0.1
Release: 1
Group: Development/Libraries
License: PD
URL: https://github.com/BurntSushi/xpybutil
Source0: xpybutil-master.zip
Requires: python3-xcffib
BuildArch: noarch

%description
xpybutil exists because xpyb is a very low level library that communicates
with X. The most mature portions of xpybutil are the ICCCM and EWMH modules.
Each implement their respective specifications of the same name. The EWMH
module also implements the '_NET_WM_WINDOW_OPACITY' and '_NET_VISIBLE_DESKTOPS'
non-standard features. The former is widely used by compositing managers and
other utilities (i.e., xcompmgr and transset-df) while the latter is used by my
fork of Openbox called Openbox Multihead.

%prep
%setup -q -n xpybutil-master
sed -i '6,13d' setup.py

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
rm -r %{buildroot}%{_datadir}/doc/%{name}

%files
%doc COPYING README
%{python3_sitelib}/*

%changelog
* Wed Aug 26 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuild for Fedora
