Name:		dkms-k10temp
Version:	20181017
Release:	1
Summary:	AMD K10 cpu sensor driver
Group:		System Environment/Kernel
License:	GPLv2+
URL:		http://khali.linux-fr.org/devel/misc/k10temp/
Source0:	k10temp-master.zip
BuildArch:	noarch
Requires:	gcc, make
Requires(post):	dkms
Requires(preun): dkms

%description
AMD K10 cpu sensor driver
  
%prep
%setup -q -n k10temp-master

%build

%install
rm -rf %{buildroot}
%define dkms_name k10temp
%define dkms_vers %{version}-%{release}
#%define quiet -q

# Kernel module sources install for dkms
mkdir -p %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
cp -a  * %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
cat > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
BUILT_MODULE_NAME[0]=%{dkms_name}
DEST_MODULE_LOCATION[0]=/kernel/drivers/hwmon
AUTOINSTALL="YES"
EOF

%clean
rm -rf %{buildroot}

%post
# Add to DKMS registry
dkms add -m %{dkms_name} -v %{dkms_vers} %{?quiet} --rpm_safe_upgrade
# Rebuild and make available for the currenty running kernel
dkms build -m %{dkms_name} -v %{dkms_vers} %{?quiet}
dkms install -m %{dkms_name} -v %{dkms_vers} %{?quiet} --force

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{dkms_vers} %{?quiet} --all --rpm_safe_upgrade

%files
%doc LICENSE README
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

%changelog
* Mon Dec 10 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20181017
- Rebuilt for Fedora
* Tue May 31 2011 LTN Packager <packager-el6rpms@LinuxTECH.NET> - 20110406-1
- initial release
