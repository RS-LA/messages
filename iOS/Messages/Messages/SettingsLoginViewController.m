//
//  SettingsLoginViewController.m
//  Messages
//
//  Created by Eyuel Tessema on 5/5/13.
//  Copyright (c) 2013 MessagesInc. All rights reserved.
//

#import "SettingsLoginViewController.h"

@interface SettingsLoginViewController ()

@end

@implementation SettingsLoginViewController

- (IBAction)loginButtonPressed {
    NSLog(@"button pressed");
}

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
