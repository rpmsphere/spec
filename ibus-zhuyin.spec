Name:       ibus-zhuyin
Version:    0.1.0
Release:    2
Summary:    IBus Traditional ZhuYin Input Method
License:    GPLv3+
Group:      System Environment/Libraries
URL:        http://fourdollars.github.com/ibus-zhuyin/
Source0:    https://github.com/fourdollars/ibus-zhuyin/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:     %{name}-%{version}.diff
BuildRequires:    ibus-devel
Requires:         ibus

%description
This traditional Chinese zhuyin input method is designed for the old school style.
There is no intelligent phonetic matching mechanism.
You have to select which word you want everytime.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
ibus restart || :

%postun
ibus restart || :

%files
%doc AUTHORS COPYING README
%{_datadir}/%{name}
%{_datadir}/ibus/component/zhuyin.xml
%{_libexecdir}/ibus-engine-zhuyin

%changelog
* Wed Nov 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Initial package

* Fri Mar 15 2013 Shih-Yuan Lee (FourDollars) <fourdollars@gmail.com>
- The first version
