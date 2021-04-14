%define fontname        arphic-pl
%define fontdir         %{_datadir}/fonts/%{fontname}

Summary: Arphic PL TrueType Fonts
Name: %{fontname}-fonts
Version: 20100309
Release: 3.1
License: APL (No Commercial Use)
Group: User Interface/X
BuildArch: noarch
Source: %{name}-%{version}.zip
Source1: %{fontname}.conf
Requires(post): fontconfig

%description
AR PLMingU20 Light, Encoding:Unicode, Charset:Unicode 2.0, Hanzi:20902
AR PLBaosong2GBK Light，Encoding:Unicode, Charset:GBK, Hanzi:21003

%prep
%setup -q -c

%build

%install
%__rm -rf $RPM_BUILD_ROOT

%__install -d $RPM_BUILD_ROOT%{fontdir}
%__install -m 644 *.ttf $RPM_BUILD_ROOT%{fontdir}

%__install -Dm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/fonts/conf.avail/68-%{fontname}.conf
%__mkdir_p %{buildroot}%{_sysconfdir}/fonts/conf.d
ln -sf ../conf.avail/68-%{fontname}.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/68-%{fontname}.conf

%clean
%__rm -rf $RPM_BUILD_ROOT

%post
[  -x /usr/bin/fc-cache ] && /usr/bin/fc-cache 2> /dev/null

%postun
[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache 2> /dev/null

%files
%doc *.pdf
%{fontdir}
%{_sysconfdir}/fonts/conf.*/68-%{fontname}.conf

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20100309
- Rebuilt for Fedora
