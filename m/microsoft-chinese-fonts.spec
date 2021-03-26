%define	fontdir	%{_datadir}/fonts/microsoft

Summary: Microsoft Chinese TrueType Fonts
Name: microsoft-chinese-fonts
Version: 2006
Release: 1%{?dist}
License: Commercial
Group: User Interface/X
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source0: kaiu.ttf
Source1: mingliu.ttc
URL: http://www.microsoft.com/
Requires(post): fontconfig

%description
Microsoft Chinese TTF Fonts include KaiU and MingLiU.

%prep
%setup -T -c
cp %{SOURCE0} %{SOURCE1} .

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{fontdir}
install -m 0644 kaiu.ttf %{buildroot}%{fontdir}
install -m 0644 mingliu.ttc %{buildroot}%{fontdir}

%clean
rm -rf %{buildroot}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%defattr(-, root, root)
%{fontdir}/*

%changelog
