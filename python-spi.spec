%define pkgname pyspi

Summary: Python binding for AT-SPI
Name: python-spi
Version: 0.6.1
Release: %mkrel 2
License: GPL
Group: Development/Python
URL: https://people.redhat.com/zcerza/dogtail/
Source0: http://people.redhat.com/zcerza/dogtail/releases/%{pkgname}-%{version}.tar.gz
# (fc) 0.6.1-1mdv fix build with latest pyrex (Debian + fcrozat)
Patch0: pyspi-0.6.1-newpyrex.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python-devel
BuildRequires: python-pyrex
BuildRequires: libat-spi-devel

Provides: pyspi

%description
Python binding for AT-SPI

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .newpyrex

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install -O2 --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%doc COPYING 
%py_platsitedir/*
