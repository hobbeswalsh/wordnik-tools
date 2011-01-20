## Defines go here

%define _topdir $TOPDIR
%define name $PACKAGE_NAME
%define version $PACKAGE_VERSION
%define installdir $INSTALL_DIR

## SPEC information goes here
Summary: $SUMMARY
Name: %{name}
Version: %{version}
Release: 1
License: Wordnik
Group: Applications/Misc
Source: $SOURCE
URL: $URL
Distribution: Linux
Vendor: Wordnik, Inc
Packager: Hudson <wordnik-ci@wordnik.com>
BuildRoot:/var/tmp/%{name}-root/
BuildArch: noarch

## Install triggers go here
%description
Wordnik API Server %{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{installdir}/versions
cp -pR %{name}-%{version} $RPM_BUILD_ROOT/%{installdir}/versions

%post
rm $RPM_BUILD_ROOT%{installdir}/current
ln -fs $RPM_BUILD_ROOT%{installdir}/versions/%{name}-%{version} %{installdir}/current
cp -up %{installdir}/versions/%{name}-%{version}/conf/* %{installdir}

%files
%{installdir}/versions/%{name}-%{version}/*
