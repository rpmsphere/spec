Summary:        Automated wireless auditor
Name:           wifite
Version:        2.2.5
Release:        1
Source0:        https://github.com/derv82/wifite2/archive/%{version}.tar.gz#/%{name}2-%{version}.tar.gz
License:        GPLv2
Group:          Internet
BuildArch:      noarch
URL:            https://github.com/derv82/wifite2
Requires:       aircrack-ng, reaver, cowpatty, hashcat, wireshark-cli
Requires:       hcxtools, hcxdumptool
Suggests:       pyrit

%description
To attack multiple WEP, WPA, and WPS encrypted networks in a row. This tool is
customizable to be automated with only a few arguments. Wifite aims to be the
"set it and forget it" wireless auditing tool.

%prep
%setup -q -n %{name}2-%{version}

%build
python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python3 setup.py install --root %{buildroot} --prefix %{_prefix}

%files
%doc *.md
%{python3_sitelib}/wifite*
%{_datadir}/dict/wordlist-top4800-probable.txt
%{_sbindir}/%{name}

%changelog
* Tue Dec 10 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.5
- Rebuilt for Fedora
