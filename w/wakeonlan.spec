Summary:	Wake-on-LAN magic packet sender
Name:		wakeonlan
Version:	0.41
Release:	3.1
Source:		http://gsd.di.uminho.pt/jpo/software/wakeonlan/downloads/%{name}-%{version}.tar.bz2
License:	Artistic
URL:		http://gsd.di.uminho.pt/jpo/software/wakeonlan/
Group:		Networking/Remote access
BuildArch:	noarch

%description
Wakeonlan is a Perl script that sends 'magic packets' to
wake-on-LAN enabled ethernet adapters and motherboards, in
order to switch on remote computers.

%prep
%setup -q

%install
rm -rf %{buildroot}
%__install -D -m755 wakeonlan %{buildroot}%{_bindir}/wakeonlan

%clean
rm -rf %{buildroot}

%files
%doc examples Changes README
%{_bindir}/wakeonlan

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.41
- Rebuild for Fedora
* Tue Dec 11 2012 Alex Burmashev <alex.burmashev@rosalab.ru> 0.41-3
+ Revision: d67eac9
- merging with rosa2012.1 of project wakeonlan
