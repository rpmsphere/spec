Summary:	Mailing list manager
Name:		rumble
Version:	0.0.23
Release:	16.1
License:	Ruby's License
Group:		Applications
Source0:	http://dinhe.net/~aredridel/projects/ruby/%{name}-%{version}.tar.gz
URL:		http://dinhe.net/~aredridel/projects/ruby/rumble
BuildRequires: ruby
BuildRequires: rubypick
BuildRequires: rubygems
BuildArch:	noarch

%description
A simple mailing list manager.

%prep
%setup -q
sed -i -e '109s|Config|RbConfig|' -e '1220s|Config|RbConfig|' setup.rb

%build
ruby setup.rb config --rb-dir=%{_datadir}/ruby/vendor_ruby
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/rumble
%{_datadir}/ruby/vendor_ruby/rumble*

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.23
- Rebuild for Fedora
* Sat Jan 22 2011 PLD Team <feedback@pld-linux.org>
Revision 1.3  2011/01/22 22:39:59  sparky
- BR: setup.rb
- dropped unused BR: ruby-rake
Revision 1.2  2010/09/11 04:14:25  aredridel
- Clean up spec
- BR: ruby-rake instead of rake
Revision 1.1  2008/06/06 17:25:29  aredridel
- added
